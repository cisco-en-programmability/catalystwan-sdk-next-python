Policy Group with NGFW deployment
=================================

This document showcases examples for deploying a Policy Group with NGFW configuration.

.. dropdown:: Feature Profile

    .. code-block:: python

        def get_feature_profile_id(client: ApiClient, feature_profile_name: str) -> str:
            results = client.v1.feature_profile.sdwan.get_sdwan_feature_profile_by_sdwan_family()
            for result in results:
                if result["profileName"] == feature_profile_name:
                    profile_id = result["profileId"]
                    return profile_id

.. dropdown:: Group of Interest

    In this example, we will create an Application List for Policy Object Feature Profile. Each Group of Interest has their own api path, following the pattern
    ``client.v1.feature_profile.sdwan.policy_object.{parcel_name}``.

    .. code-block:: python

        def create_app_list(client: ApiClient, policy_object_profile_id: str) -> str:
            # Define AppList
            app_list = client.v1.feature_profile.sdwan.policy_object.app_list
            entries = [
                app_list.m.Entries1(app=app_list.m.OneOfEntriesAppOptionsDef(option_type="global", value="test-app-1")),
                app_list.m.Entries1(app=app_list.m.OneOfEntriesAppOptionsDef(option_type="global", value="test-app-2")),
                app_list.m.Entries2(app_family=app_list.m.OneOfEntriesAppFamilyOptionsDef(option_type="global", value="test-app-family-1")),
            ]
            payload = app_list.m.Default(
                name="TEST_APP_LIST",
                data=app_list.m.Data(entries=entries),
            )
            # Create AppList
            parcel_id = app_list.create_data_prefix_profile_parcel_for_security_policy_object(policy_object_profile_id, payload).parcel_id
            return parcel_id


        def delete_app_list(client: ApiClient, profile_id: str, parcel_id: str):
            client.v1.feature_profile.sdwan.policy_object.delete_data_prefix_profile_parcel_for_policy_object(
                profile_id, policy_object_list_type="app-list", list_object_id=parcel_id
            )

.. dropdown:: Embedded Security Profile

    .. code-block:: python

        def create_embedded_security_profile(client: ApiClient) -> str:
            es_api = client.v1.feature_profile.sdwan.embedded_security
            # Define Embedded Security Profile
            es = es_api.m.EmbeddedSecurityDefault(name="TEST_EMBEDDED_SECURITY", description="TEST_EMBEDDED_SECURITY")
            # Create Embedded Security Profile
            es_response = es_api.create_sdwan_embedded_security_feature_profile(es)
            return es_response.id


        def delete_embedded_security_profile(client: ApiClient, profile_id: str):
            # Detaching or removing a Policy Group may be needed first.
            es_api = client.v1.feature_profile.sdwan.embedded_security
            es_api.delete_sdwan_embedded_security_feature_profile(profile_id)


        def copy_embedded_security_profile(client: ApiClient, profile_id: str) -> str:
            es_api = client.v1.feature_profile.sdwan.embedded_security
            es = es_api.m.EmbeddedSecurityDefault(
                name="TEST_EMBEDDED_SECURITY2",
                description="TEST_EMBEDDED_SECURITY2",
                from_feature_profile=es_api.m.FromFeatureProfileDef(copy=profile_id)
            )
            return es_api.create_sdwan_embedded_security_feature_profile(es).id

.. dropdown:: NGFW Parcel

    In this example we will create an NGFW Parcel for Embedded Security Profile

    .. code-block:: python

        def create_ngfw_parcel(client: ApiClient, es_profile_id: str) -> str:
            ngfw_api = client.v1.feature_profile.sdwan.embedded_security.unified.ngfirewall
            m = ngfw_api.m
            # Define NGFW Parcel
            ngfw_parcel = m.Default(
                name="TEST_NGFW_PARCEL",
                description="TEST_NGFW_PARCEL",
                data=m.Data(
                    default_action_type=m.OneOfDefaultActionTypeOptionsDef(value="pass", option_type="global"),
                    sequences=[
                        m.Sequences(
                            actions=[],
                            sequence_id=m.OneOfSequencesSequenceIdOptionsDef(value="1", option_type="global"),
                            sequence_name=m.OneOfSequencesSequenceNameOptionsDef(value="Rule1", option_type="global"),
                            sequence_type=m.OneOfSequencesSequenceTypeOptionsDef(option_type="global", value="ngfirewall"),
                            base_action=m.OneOfSequencesBaseActionOptionsDef(value="pass", option_type="global"),
                            disable_sequence=m.OneOfdisableSequenceDef(value=False, option_type="global"),
                            # Keep in mind: each Entries model may contain only a single rule. To add another rule, append
                            # another Entries object to the list.
                            match_=m.Match(
                                entries=[
                                    m.Entries(
                                        source_ip=m.Ipv4MatchDef(
                                            ipv4_value=m.Ipv4InputDef1(option_type="global", value=["12.0.0.0/8"])
                                        )
                                    ),
                                    m.Entries(
                                        # You can also use a device variable, to set the value later.
                                        destination_ip=m.Ipv4MatchDef(ipv4_value=m.Ipv4InputDef2(option_type="variable", value="{{test}}"))
                                    )
                                ]
                            ),
                        )
                    ],
                ),
            )
            # Create NGFW Parcel
            ngfw_response = (
                client.v1.feature_profile.sdwan.embedded_security.unified.ngfirewall.create_ngfirewall_profile_parcel(
                    es_profile_id, payload=ngfw_parcel
                )
            )
            return ngfw_response.parcel_id


        def delete_ngfw_parcel(client: ApiClient, es_profile_id: str, ngfw_id: str):
            ngfw_api = client.v1.feature_profile.sdwan.embedded_security.unified.ngfirewall
            ngfw_api.delete_ngfirewall_profile_parcel(es_profile_id, ngfw_id)

.. dropdown:: Security Policy

    In this example, we will create a Security Policy for Embedded Security Profile, with NGFW Parcel attached.

    .. code-block:: python

        def create_security_policy(client: ApiClient, profile_id: str, ngfw_id: str) -> str:
            po_api = client.v1.feature_profile.sdwan.embedded_security.policy
            m = po_api.m
            # Define Security Policy
            policy = m.Default(
                name="TEST_SECURITY_POLICY",
                description="desc",
                data=m.Data(
                    settings=m.Settings(
                        security_logging=m.NetworkSettingsOptionTypeObjectDef(option_type="network-settings", value=True)
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
                    ]
                ),
            )
            # Create Security Policy Parcel
            response = po_api.create_embedded_security_profile_parcel(profile_id, policy)
            return response["parcelId"]


        def delete_security_policy(client: ApiClient, profile_id: str, policy_id: str):
            po_api = client.v1.feature_profile.sdwan.embedded_security.policy
            po_api.delete_security_profile_parcel_1(profile_id, policy_id)

.. dropdown:: Policy Group

    In this example, we will create a Policy Group with Embedded Security Profile attached.

    .. code-block:: python

        def create_policy_group(client: ApiClient, policy_object_id: str, embedded_security_id: str) -> str:
            pg_api = client.v1.policy_group
            # Attach required profiles to the Policy Group
            profiles = [pg_api.m.ProfileIdObjDef(id=id) for id in [policy_object_id, embedded_security_id]]
            # Define Policy Group
            policy_group = pg_api.m.PolicyGroupDefault(
                name="TEST_POLICY_GROUP", description="descr", solution="sdwan", profiles=profiles
            )
            # Create Policy Group
            policy_group_id = pg_api.create_policy_group(payload=policy_group).id

            return policy_group_id


        def delete_policy_group(client: ApiClient, policy_group_id: str):
            # You may need to delete device associations first (see Associate Device example)
            pg_api = client.v1.policy_group
            pg_api.delete_policy_group(policy_group_id)


        def copy_policy_group(client: ApiClient, policy_group_id: str) -> str:
            pg_api = client.v1.policy_group
            policy_group = pg_api.m.PolicyGroupDefault(
                name="TEST_POLICY_GROUP2",
                description="descr",
                solution="sdwan",
                from_policy_group=pg_api.m.FromPolicyGroupDef(copy=policy_group_id)
            )
            return pg_api.create_policy_group(payload=policy_group).id

.. dropdown:: Get Device id

    .. code-block:: python

        def get_device_id(client: ApiClient, hostname: str) -> str:
            devices = client.device.list_all_devices()
            # You find desired device by filtering with different fields, as well.
            device = [device for device in devices if device.host_name == hostname][0]
            
            return device.uuid

.. dropdown:: Associate Device with Policy Group

    .. code-block:: python

        def associate_device(client: ApiClient, policy_group_id: str, device_id: str) -> str:
            pg_api = client.v1.policy_group
            m = pg_api.device.associate.m
            payload = m.Default(devices=[m.DeviceIdDef(id=device_id)])
            pg_api.device.associate.create_policy_group_association(policy_group_id, payload)


        def delete_association(client: ApiClient, policy_group_id: str, device_id: str):
            pg_api = client.v1.policy_group
            m = pg_api.device.associate.m
            payload = m.Default(devices=[m.DeviceIdDef(id=device_id)])
            client.v1.policy_group.device.associate.delete_policy_group_association(policy_group_id, payload)

.. dropdown:: Policy Group Variables

    .. code-block:: python

        def fetch_variables(client: ApiClient, policy_group_id: str, device_id: str) -> list:
            variables_api = client.v1.policy_group.device.variables
            payload = variables_api.m.VariablesDefault(device_ids=[device_id], suggestions=True)
            response = variables_api.fetch_policy_group_device_variables(policy_group_id, payload)
            return response["devices"]


        def set_variable_values(client: ApiClient, policy_group_id: str, devices: list):
            variables_api = client.v1.policy_group.device.variables
            m = variables_api.m
            device_variables = []
            # Using list of variables for each device, set values for them
            for device in devices:
                device_id = device["device-id"]
                variables = device["variables"]
                current_variables = []
                for variable in variables:
                    value = get_variable_value(device_id, variable["name"]) # Get variable value, i.e from config
                    current_variables.append(m.Variables(variable["name"], [value]))
                if current_variables:
                    device_variables.append(m.Devices(device_id, current_variables))
            payload = m.Default(devices=device_variables, solution="sdwan")
            variables_api.create_policy_group_device_variables(policy_group_id, payload)

.. dropdown:: Deploy Policy Group

    .. code-block:: python

        def deploy_policy_group(client: ApiClient, policy_group_id: str, device_id) -> str:

            pg_api = client.v1.policy_group.device.deploy
            m = pg_api.m
            
            payload = m.Default(
                devices=[m.DeviceIdDef(id=device_id)]
            )
            response = pg_api.deploy_policy_group(policy_group_id, payload)
            return response["parentTaskId"]

.. dropdown:: Check Task Status

    .. code-block:: python

        def check_status(client: ApiClient, task_id: str) -> bool:
            status_api = client.device.action.status
            while True:
                response = status_api.find_status(task_id)
                statuses = [status["status"] for status in response]
                if "In progress" in statuses:
                    sleep(5)
                elif "Failure" in statuses:
                    return False
                else:
                    return True

.. dropdown:: Policy Group with NGFW flow

    Entire flow, using functions from examples above
    
    .. code-block:: python

        def main(client: ApiClient):
            # Get Policy Object
            policy_object_id = get_feature_profile_id(client, name="policy_object_name")
            # Create Group of Interest for Policy Object
            create_app_list(client, policy_object_id)
            # Create Embedded Security Profile
            embedded_security_id = create_embedded_security_profile(client)
            # Create NGFW Parcel for Embedded Security Profile
            ngfw_id = create_ngfw_parcel(client, embedded_security_id)
            # Create Security Policy for Embedded Security Profile with NGFW
            create_security_policy(client, embedded_security_id, ngfw_id)
            # Create Policy Group with Embedded Security Profile
            policy_group_id = create_policy_group(client, policy_object_id, embedded_security_id)
            # Get target device
            device_id = get_device_id(client, hostname="device_hostname")
            # Associate device
            associate_device(client, policy_group_id, device_id)
            # Get and set variables values
            variables = fetch_variables(client, policy_group_id, device_id)
            set_variable_values(client, policy_group_id, variables)
            # Deploy
            task_id = deploy_policy_group(client, policy_group_id, device_id)
            # Wait for status
            status = check_status(client, task_id)
            print(status)
