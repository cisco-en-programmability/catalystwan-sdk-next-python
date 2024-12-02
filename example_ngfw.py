import typing as t

import urllib3
from catalystwan.core.client import create_client
from catalystwan.core.request_limiter import RequestLimiter
from catalystwan.core.vmanage_auth import create_vmanage_auth

# from catalystwan.versions import load_client
# from catalystwan.versions.v20_14.api_client import ApiClient


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


device_ids = [1] * 100
auth = create_vmanage_auth("admin", "Cisco#123@Viptela")
limiter = RequestLimiter(max_requests=60)


def main():
    with create_client(
        url="172.22.219.19",
        username="admin",
        password="Cisco#123@Viptela",
        port=9912,
        # auth=
        # request_lmiter=limiter,
    ) as client:
        pg_api = client.v1.policy_group
        policy_group = pg_api.create_policy_group(
            pg_api.models.PolicyGroupDefault(
                name="psm-policy-group", description="descr", solution="sdwan"
            )
        )
        ps = pg_api.get_policy_group_by_solution()
        for p in ps:
            print(p)
        pg_api.delete_policy_group(policy_group.id)
        return

        profile_id = find_default_sdwan_feature_profile_id(client)
        print(profile_id)

        esn = client.v1.feature_profile.sdwan.embedded_security
        esc = esn.create_sdwan_embedded_security_feature_profile
        es_item = esc(esc.create_payload(name="psm-test", description="psm-descr"))
        print(es_item)

        ngfw_api = client.v1.feature_profile.sdwan.embedded_security.unified.ngfirewall
        ngfw_parcel = build_ngfw_parcel(ngfw_api.models)
        pf = ngfw_api.create_ngfirewall_profile_parcel(es_item.id, ngfw_parcel)
        print(pf)

        po_api = client.v1.feature_profile.sdwan.embedded_security.policy
        policy = build_security_policy(po_api.models, pf.parcel_id)
        print(policy)
        po_api.create_embedded_security_profile_parcel(es_item.id, policy)

        input("Enter to end...")
        esn.delete_sdwan_embedded_security_feature_profile(es_item.id)
        return
        app_list_parcel = create_app_list_parcel(
            client,
            profile_id,
            app_names=["test-app-1", "test-app-2"],
            app_family_names=["test-app-family-1"],
        )
        remove_app_list_parcel(client, profile_id, app_list_parcel.parcel_id)


def print_ess(client):
    print("*" * 100)
    items = client.v1.feature_profile.sdwan.embedded_security.get_sdwan_embedded_security_feature_profiles()
    for item in items:
        print("-" * 100)
        print(item)
        c = client.v1.feature_profile.sdwan.embedded_security.get_sdwan_embedded_security_feature_profile_by_profile_id(
            item.profile_id
        )
        print(c)
    print("*" * 100)


def build_security_policy(models, ngfw_id):
    return models.Default(
        name="psm-test-security-name",
        description="desc",
        data=models.Data(
            assembly=[
                models.Assembly2(
                    ngfirewall=models.NgFirewallDef(
                        entries=[
                            models.Entries(
                                dst_zone=models.ZoneDef2(value="self", option_type="global"),
                                src_zone=models.ZoneDef2(value="untrusted", option_type="global"),
                            )
                        ],
                        ref_id=models.RefIdDef(value=ngfw_id, option_type="global"),
                    )
                )
            ]
        ),
    )


def build_ngfw_parcel(models):
    return models.Default(
        name="psm-ngfw",
        description="desc",
        data=models.Data(
            default_action_type=models.OneOfDefaultActionTypeOptionsDef(
                value="drop", option_type="global"
            ),
            sequences=[
                models.Sequences(
                    actions=[],
                    sequence_id=models.OneOfSequencesSequenceIdOptionsDef(
                        value="1", option_type="global"
                    ),
                    sequence_name=models.OneOfSequencesSequenceNameOptionsDef(
                        value="seq-1", option_type="global"
                    ),
                    sequence_type=models.OneOfSequencesSequenceTypeOptionsDef(
                        option_type="global", value="ngfirewall"
                    ),
                    base_action=models.OneOfSequencesBaseActionOptionsDef(
                        value="drop", option_type="global"
                    ),
                    match_=models.Match(
                        entries=[
                            models.Entries(
                                source_ip=models.Ipv4MatchDef(
                                    ipv4_value=models.Ipv4InputDef1(
                                        option_type="global", value=["10.0.0.1/16"]
                                    )
                                )
                            )
                        ]
                    ),
                )
            ],
        ),
    )


def create_app_list_parcel(
    client,
    profile_id: str,
    *,
    app_names: t.Optional[t.List[str]] = None,
    app_family_names: t.Optional[t.List[str]] = None,
):
    app_list = client.v1.feature_profile.sdwan.policy_object.app_list.create_data_prefix_profile_parcel_for_security_policy_object()

    # result = app_list.create_data_prefix_profile_parcel_for_security_policy_object(
    # profile_id, {"name": "test", "data": {"entries": [{"app": {"optionType": "global", "value": "test"}}]}}
    # )
    entries = []
    entries += [
        app_list.models.Entries1(app={"optionType": "global", "value": name})
        for name in app_names or []
    ]
    entries += [
        app_list.models.Entries2(app_family={"optionType": "global", "value": name})
        for name in app_family_names or []
    ]
    payload = app_list.models.Default(
        name="test",
        data=app_list.models.Data(entries=entries),
    )
    parcel_id = app_list.create_data_prefix_profile_parcel_for_security_policy_object(
        profile_id, payload
    ).parcel_id
    return app_list.get_data_prefix_profile_parcel_for_policy_object(profile_id, parcel_id)


def remove_app_list_parcel(client, profile_id: str, parcel_id: str) -> None:
    client.v1.feature_profile.sdwan.policy_object.delete_data_prefix_profile_parcel_for_policy_object(
        profile_id, "app-list", parcel_id
    )


def find_default_sdwan_feature_profile_id(client, name="Default_Policy_Object_Profile"):
    results = client.v1.feature_profile.sdwan.get_sdwan_feature_profile_by_sdwan_family()
    for result in results:
        if result["profileName"] == name:
            return result["profileId"]
    raise ValueError(f"Not found profile with name: {name}")


if __name__ == "__main__":
    main()
