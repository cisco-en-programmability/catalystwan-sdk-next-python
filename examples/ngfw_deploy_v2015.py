from __future__ import annotations

import os
from dataclasses import dataclass
from time import sleep
from typing import TYPE_CHECKING

import urllib3
from catalystwan.core.client import create_client
from dotenv import find_dotenv, load_dotenv

if TYPE_CHECKING:
    from catalystwan.core.loader import ApiClient


load_dotenv(find_dotenv(usecwd=True))
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


SDWAN_URL = os.environ["SDWAN_URL"]
SDWAN_PORT = int(os.environ["SDWAN_PORT"])
SDWAN_USERNAME = os.environ["SDWAN_USERNAME"]
SDWAN_PASSWORD = os.environ["SDWAN_PASSWORD"]
POLICY_OBJECT_PROFILE_NAME = "Policy_Object_Name"
DEVICE_HOSTNAME = "Device_Hostname"

POLICY_OBJECT_PROFILE_NAME = "Default_Policy_Object_Profile"
DEVICE_HOSTNAME = "vm1"


@dataclass
class Step1Results:
    policy_object_profile_id: str
    app_list_id: str


@dataclass
class Step2Results:
    embedded_security_id: str
    ngfw_parcel_id: str
    security_policy_id: str


@dataclass
class Step3Results:
    policy_group_id: str


@dataclass
class Step4Results:
    device_id: str
    task_id: str


def get_feature_profile_id(client: ApiClient, feature_profile_name: str) -> str:
    results = client.v1.feature_profile.sdwan.get()
    for result in results:
        if result.profile_name == feature_profile_name:
            profile_id = result.profile_id
            return profile_id


def create_app_list(client: ApiClient, policy_object_profile_id: str) -> str:
    # Define AppList
    app_list = client.v1.feature_profile.sdwan.policy_object.app_list
    entries = [
        app_list.m.Entries1(
            app=app_list.m.OneOfEntriesAppOptionsDef(option_type="global", value="test-app-1")
        ),
        app_list.m.Entries1(
            app=app_list.m.OneOfEntriesAppOptionsDef(option_type="global", value="test-app-2")
        ),
        app_list.m.Entries2(
            app_family=app_list.m.OneOfEntriesAppFamilyOptionsDef(
                option_type="global", value="test-app-family-1"
            )
        ),
    ]
    payload = app_list.m.CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest(
        name="TEST2_APP_LIST",
        data=app_list.m.Data(entries=entries),
    )
    # Create AppList
    parcel_id = app_list.post(
        policy_object_profile_id, payload
    ).parcel_id
    return parcel_id


def delete_app_list(client: ApiClient, policy_object_id: str, app_list_id: str):
    client.v1.feature_profile.sdwan.policy_object.delete(
        policy_object_id, policy_object_list_type="app-list", list_object_id=app_list_id
    )


def define_security_objects(client: ApiClient, feature_profile_name: str) -> Step1Results:
    ### Define security objects (group of interest)
    # Get Policy Object Profile. We will associate other objects with it.
    profile_id = get_feature_profile_id(client, feature_profile_name)
    print(f"Found Policy Object Profile profile with id {profile_id}\n")

    # Create required parcels to associate with Policy Object Profile
    parcel_id = create_app_list(client, profile_id)
    print(f"Created AppList policy object with id {parcel_id}\n")

    return Step1Results(policy_object_profile_id=profile_id, app_list_id=parcel_id)


def create_embedded_security_profile(client: ApiClient) -> str:
    es_api = client.v1.feature_profile.sdwan.embedded_security
    # Define Embedded Security Profile
    es = es_api.m.CreateSdwanEmbeddedSecurityFeatureProfilePostRequest(
        name="DEMO_NGFW_EMBEDDED_SECURITY", description="EmbeddedSecurity_Test"
    )
    # Create Embedded Security Profile
    es_response = es_api.post(es)
    return es_response.id


def delete_embedded_security_profile(client: ApiClient, es_profile_id: str):
    es_api = client.v1.feature_profile.sdwan.embedded_security
    es_api.delete(es_profile_id)


def copy_embedded_security_profile(client: ApiClient, es_profile_id: str) -> str:
    es_api = client.v1.feature_profile.sdwan.embedded_security
    es = es_api.m.CreateSdwanEmbeddedSecurityFeatureProfilePostRequest(
        name="TEST_EMBEDDED_SECURITY2",
        description="TEST_EMBEDDED_SECURITY2",
        from_feature_profile=es_api.m.FromFeatureProfileDef(copy=es_profile_id),
    )
    return es_api.post(es).id


def create_ngfw_parcel(client: ApiClient, es_profile_id: str) -> str:
    ngfw_api = client.v1.feature_profile.sdwan.embedded_security.unified.ngfirewall
    m = ngfw_api.m
    # Define NGFW Parcel
    ngfw_parcel = m.CreateNgfirewallProfileParcelPostRequest(
        name="DEMO_NGFW_NGFW_PARCEL",
        description="NGFW_TEST",
        data=m.UnifiedNgfirewallData(
            default_action_type=m.OneOfDefaultActionTypeOptionsDef(
                value="pass", option_type="global"
            ),
            sequences=[
                m.Sequences(
                    actions=[],
                    sequence_id=m.OneOfSequencesSequenceIdOptionsDef(
                        value="1", option_type="global"
                    ),
                    sequence_name=m.OneOfSequencesSequenceNameOptionsDef(
                        value="Rule1", option_type="global"
                    ),
                    sequence_type=m.OneOfSequencesSequenceTypeOptionsDef(
                        option_type="global", value="ngfirewall"
                    ),
                    base_action=m.OneOfSequencesBaseActionOptionsDef(
                        value="pass", option_type="global"
                    ),
                    disable_sequence=m.OneOfdisableSequenceDef(value=False, option_type="global"),
                    # Keep in mind: each Entries model may contain only a single rule. To add another rule, append
                    # another Entries object to the list.
                    match_=m.Match(
                        entries=[
                            m.Entries(
                                source_ip=m.Ipv4MatchDef(
                                    ipv4_value=m.Ipv4InputDef1(
                                        option_type="global", value=["12.0.0.0/8"]
                                    )
                                )
                            ),
                            m.Entries(
                                # You can also use a device variable, to set the value later.
                                destination_ip=m.Ipv4MatchDef(
                                    ipv4_value=m.Ipv4InputDef2(
                                        option_type="variable", value="{{destination_ip_var}}"
                                    )
                                )
                            ),
                        ]
                    ),
                )
            ],
        ),
    )
    # Create NGFW Parcel
    ngfw_response = client.v1.feature_profile.sdwan.embedded_security.unified.ngfirewall.post(
        es_profile_id, payload=ngfw_parcel
    )
    return ngfw_response.parcel_id


def delete_ngfw_parcel(client: ApiClient, es_profile_id: str, ngfw_id: str):
    ngfw_api = client.v1.feature_profile.sdwan.embedded_security.unified.ngfirewall
    ngfw_api.delete(es_profile_id, ngfw_id)


def create_security_policy(client: ApiClient, es_profile_id: str, ngfw_id: str) -> str:
    po_api = client.v1.feature_profile.sdwan.embedded_security.policy
    m = po_api.m
    # Define Security Policy
    policy = m.CreateEmbeddedSecurityProfileParcelPostRequest(
        name="DEMO_NGFW_SECURITY_POLICY",
        description="desc",
        data=m.EmbeddedSecurityPolicyData(
            settings=m.Settings(
                security_logging=m.NetworkSettingsOptionTypeObjectDef(
                    option_type="network-settings", value=True
                )
            ),
            assembly=[
                m.Assembly2(
                    ngfirewall=m.NgFirewallDef(
                        entries=[
                            m.Entries(
                                dst_zone=m.ZoneDef2(value="untrusted", option_type="global"),
                                src_zone=m.ZoneDef2(value="default", option_type="global"),
                            )
                        ],
                        ref_id=m.RefIdDef(value=ngfw_id, option_type="global"),
                    )
                )
            ],
        ),
    )
    # Create Security Policy Parcel
    response = po_api.post(es_profile_id, policy)
    return response.parcel_id


def delete_security_policy(client: ApiClient, es_profile_id: str, security_policy_id: str):
    po_api = client.v1.feature_profile.sdwan.embedded_security.policy
    po_api.delete(es_profile_id, security_policy_id)


def new_ngfw_policy(client: ApiClient) -> Step2Results:
    # Create Embedded Security Feature Profile
    profile_id = create_embedded_security_profile(client)
    print(f"Created Embedded Security Profile with id {profile_id}\n")

    # Create NGFW Parcel
    ngfw_id = create_ngfw_parcel(client, profile_id)
    print(f"Created NGFW Parcel with id {ngfw_id}\n")

    # Combine Embedded Security and NGFW with Security Policy
    security_policy_id = create_security_policy(client, profile_id, ngfw_id)
    print(f"Created Security Policy with id {security_policy_id}\n")

    return Step2Results(
        embedded_security_id=profile_id,
        ngfw_parcel_id=ngfw_id,
        security_policy_id=security_policy_id,
    )


def create_policy_group(client: ApiClient, policy_object_id: str, embedded_security_id: str) -> str:
    pg_api = client.v1.policy_group
    # Attach required profiles to the Policy Group
    profiles = [pg_api.m.ProfileIdObjDef(id=id) for id in [policy_object_id, embedded_security_id]]
    # Define Policy Group
    policy_group = pg_api.m.CreatePolicyGroupPostRequest(
        name="DEMO_NGFW_POLICY_GROUP", description="descr", solution="sdwan", profiles=profiles
    )
    # Create Policy Group
    policy_group_id = pg_api.post(payload=policy_group).id

    return policy_group_id


def delete_policy_group(client: ApiClient, policy_group_id: str):
    pg_api = client.v1.policy_group
    pg_api.delete(policy_group_id)


def copy_policy_group(client: ApiClient, policy_group_id: str) -> str:
    pg_api = client.v1.policy_group
    policy_group = pg_api.m.CreatePolicyGroupPostRequest(
        name="TEST_POLICY_GROUP2",
        description="descr",
        solution="sdwan",
        from_policy_group=pg_api.m.FromPolicyGroupDef(copy=policy_group_id),
    )
    return pg_api.post(payload=policy_group).id


def create_policy_group_with_ngfw(
    client: ApiClient, policy_object_id: str, embedded_security_id: str
) -> Step3Results:
    # Create Policy Group Object and attach Embedded Security to it
    policy_group_id = create_policy_group(client, policy_object_id, embedded_security_id)
    print(f"Created Policy Group with id {policy_group_id}\n")

    return Step3Results(policy_group_id)


def get_device_id(client: ApiClient, hostname: str) -> str:
    devices = client.device.get()
    print([d.host_name for d in devices])
    # You find desired device by filtering with different fields, as well.
    device = [device for device in devices if device.host_name == hostname][0]
    return device.uuid


def get_device(client: ApiClient, personality="vedge") -> str:
    devices = client.device.list_all_devices()
    filtered_devices = [device for device in devices if device.personality == personality]

    return filtered_devices


def associate_device(client: ApiClient, policy_group_id: str, device_id: str) -> str:
    pg_api = client.v1.policy_group
    m = pg_api.device.associate.m
    payload = m.CreatePolicyGroupAssociationPostRequest(devices=[m.DeviceIdDef(id=device_id)])
    pg_api.device.associate.post(policy_group_id, payload)


def delete_association(client: ApiClient, policy_group_id: str, device_id: str):
    pg_api = client.v1.policy_group
    m = pg_api.device.associate.m
    payload = m.DeletePolicyGroupAssociationDeleteRequest(devices=[m.DeviceAssociateDeviceIdDef(id=device_id)])
    client.v1.policy_group.device.associate.delete(
        policy_group_id, payload
    )


def set_variable_values(client: ApiClient, policy_group_id: str, device_id: str):
    variables_api = client.v1.policy_group.device.variables
    m = variables_api.m

    # Fetch variables
    fetch_variables_payload = m.FetchPolicyGroupDeviceVariablesPostRequest(
        device_ids=[device_id], suggestions=True
    )
    device_variables = variables_api.post(
        policy_group_id, fetch_variables_payload
    ).devices

    set_variables_payload = []
    # Using list of variables for each device, set values for them
    for device_variable in device_variables:
        device_id = device_variable.device_id
        variables = device_variable.variables
        current_variables = []
        for variable in variables:
            value = input(f"[Device {device_id}] Enter value for variable {variable.name}: ")
            current_variables.append(m.Variables(variable.name, [value]))
        if current_variables:
            set_variables_payload.append(m.Devices(device_id, current_variables))
    payload = m.CreatePolicyGroupDeviceVariablesPutRequest(
        devices=set_variables_payload, solution="sdwan"
    )
    variables_api.put(policy_group_id, payload)


def deploy_policy_group(client: ApiClient, policy_group_id: str, device_id) -> str:
    pg_api = client.v1.policy_group.device.deploy
    m = pg_api.m

    payload = m.DeployPolicyGroupPostRequest(devices=[m.DeviceIdDef(id=device_id)])
    response = pg_api.post(policy_group_id, payload)
    return response.parent_task_id


def deploy(client: ApiClient, policy_group_id: str, device_hostname: str) -> Step4Results:
    device_id = get_device_id(client, device_hostname)
    # Associate device with Policy Group
    associate_device(client, policy_group_id, device_id)
    print(f"Associated Device {device_id} with Policy Group {policy_group_id}")
    # Set variables for devices
    set_variable_values(client, policy_group_id, device_id)
    # Deploy Policy Group to devices
    task_id = deploy_policy_group(client, policy_group_id, device_id)
    print("Deployed")

    return Step4Results(device_id=device_id, task_id=task_id)


def check_status(client: ApiClient, task_id: str) -> bool:
    status_api = client.device.action.status
    while True:
        response = status_api.get(task_id)
        print(response)
        statuses = [status["status"] for status in response]
        if "In progress" in statuses:
            print("In progress...\n")
            sleep(5)
        elif "Failure" in statuses:
            return False
        else:
            return True


def cleanup(
    client: ApiClient,
    step1_results: Step1Results,
    step2_results: Step2Results,
    step3_results: Step3Results,
    step4_results: Step4Results,
):
    delete_app_list(client, step1_results.policy_object_profile_id, step1_results.app_list_id)
    print(f"Policy object AppList with id {step1_results.app_list_id} deleted\n")

    delete_security_policy(
        client, step2_results.embedded_security_id, step2_results.security_policy_id
    )
    print(f"Security Policy with id {step1_results.app_list_id} deleted\n")
    delete_ngfw_parcel(client, step2_results.embedded_security_id, step2_results.ngfw_parcel_id)
    print(f"NGFW Parcel with id {step2_results.ngfw_parcel_id} deleted\n")

    delete_association(client, step3_results.policy_group_id, step4_results.device_id)
    delete_policy_group(client, step3_results.policy_group_id)
    print(f"Policy Group with id {step3_results.policy_group_id} deleted.\n")

    delete_embedded_security_profile(client, step2_results.embedded_security_id)
    print(f"Embedded Security Profile with id {step2_results.embedded_security_id} deleted.\n")


def main():
    with create_client(
        url=SDWAN_URL,
        port=SDWAN_PORT,
        username=SDWAN_USERNAME,
        password=SDWAN_PASSWORD,
    ) as client:
        input("STEP 1. Define security objects (group of interest). Press Enter to continue.\n")
        step1_results = define_security_objects(
            client, feature_profile_name=POLICY_OBJECT_PROFILE_NAME
        )
        print("-" * 100)
        input("STEP 2. Define new NGFW policy. Press Enter to continue.\n")
        step2_results = new_ngfw_policy(client)
        print("-" * 100)
        input(
            "STEP 3. Define new policy group and add a NGFW policy to such a group. Press Enter to continue.\n"
        )
        step3_results = create_policy_group_with_ngfw(
            client, step1_results.policy_object_profile_id, step2_results.embedded_security_id
        )
        print("-" * 100)
        input("STEP 4. Deploy a policy group to a group of devices. Press Enter to continue.\n")
        step4_results = deploy(
            client, step3_results.policy_group_id, device_hostname=DEVICE_HOSTNAME
        )
        print("-" * 100)
        sleep(2)
        print("Waiting for status...\n")
        deploy_status = check_status(client, step4_results.task_id)
        print(f"Deploy finished with status: {deploy_status}.\n")
        cleanup_input = input("Perform CLEANUP. Y/N?\n")
        if cleanup_input.lower() == "y":
            cleanup(client, step1_results, step2_results, step3_results, step4_results)


if __name__ == "__main__":
    main()
