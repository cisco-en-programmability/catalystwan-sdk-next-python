====
NGFW
====

Connect to server
=================

.. code:: python

    with create_client( url="0.0.0.0", username="admin", password="password", port=9912,) as client:
        ...

List of feature profiles
------------------------

Find default Default_Policy_Object_Profile:

.. code:: python

    results = client.v1.feature_profile.sdwan.get_sdwan_feature_profile_by_sdwan_family()
    for result in results:
        if result["profileName"] == "Default_Policy_Object_Profile":
            print(result)
            profile_id = result["profileId"]


.. code:: json

    {
      "profileId": "6d4931e3-9dfc-45e6-9135-6701405d7562",
      "profileName": "Default_Policy_Object_Profile",
      "solution": "sdwan",
      "profileType": "policy-object",
      "createdBy": "system",
      "lastUpdatedBy": "admin",
      "createdOn": 1711047593766,
      "description": "Default profile for Policy-Objects",
      "lastUpdatedOn": 1736947423330
    }

Create required parcels
-----------------------

.. code:: python

    # make alias 
    po_api = client.v1.feature_profile.sdwan.policy_object
    app_list_api = po_api.app_list
    
    # prepare payload data
    entries = [
        app_list_api.m.Entries1(app={"optionType": "global", "value": "test-api-1"})
        app_list_api.m.Entries1(app={"optionType": "global", "value": "test-api-2"})
        app_list_api.m.Entries2(app_family={"optionType": "global", "value": "test-app-family-1"})
    ]
    payload = app_list_api.m.Default(
        name="test",
        data=app_list_api.m.Data(entries=entries),
    )

    # create AppList Parcel
    parcel_id = app_list_api.create_data_prefix_profile_parcel_for_security_policy_object(
        profile_id, payload
    ).parcel_id

    # load AppList Parcel
    parcel = app_list_api.get_data_prefix_profile_parcel_for_policy_object(
        profile_id, parcel_id
    )

    # delete AppList parcel
    po_api.delete_data_prefix_profile_parcel_for_policy_object(
        profile_id, "app-list", parcel_id
    )

Create Policy Group
-------------------

.. code:: python
    
    # alias
    pg_api = client.v1.policy_group
    
    # build model
    model = pg_api.m.PolicyGroupDefault(
        name="psm-policy-group", description="descr", solution="sdwan"
    )

    # create policy group
    policy_group_id = pg_api.create_policy_group(model).id

    # load exists policy group
    policy_group = pg_api.get_policy_group(policy_group_id)

    # delete exists policy group 
    pg_api.delete_policy_group(policy_group_id)


Associate Policy Group to device
--------------------------------

.. code:: python

    policy_group_id = # ...

    pg_api = client.v1.policy_group
    
    # find device (get first)
    ds = client.system.device.get_devices_details("vedges")[0]


    # build model
    m = pg_api.device.associate.m
    ad = m.Default(devices=[m.DeviceIdDef(id=ds["uuid"])])

    # craete association
    pg_api.device.associate.create_policy_group_association(policy_group_id, ad)
    
    # load policy group association
    ads = pg_api.device.associate.get_policy_group_association(policy_group_id)

Create Embedded Security in Policy Group
----------------------------------------

.. code:: python
    
    # define sample ngfirewall model

    def build_ngfw_parcel(m):
        return m.Default(
            name="psm-ngfw",
            description="desc",
            data=m.Data(
                default_action_type=m.OneOfDefaultActionTypeOptionsDef(
                    value="drop", option_type="global"
                ),
                sequences=[
                    m.Sequences(
                        actions=[],
                        sequence_id=m.OneOfSequencesSequenceIdOptionsDef(
                            value="1", option_type="global"
                        ),
                        sequence_name=m.OneOfSequencesSequenceNameOptionsDef(
                            value="seq-1", option_type="global"
                        ),
                        sequence_type=m.OneOfSequencesSequenceTypeOptionsDef(
                            option_type="global", value="ngfirewall"
                        ),
                        base_action=m.OneOfSequencesBaseActionOptionsDef(
                            value="drop", option_type="global"
                        ),
                        match_=m.Match(
                            entries=[
                                m.Entries(
                                    source_ip=m.Ipv4MatchDef(
                                        ipv4_value=m.Ipv4InputDef1(
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
    
    # define sample security policy
    def build_security_policy(m, ngfw_id):
        return m.Default(
            name="psm-test-security-name",
            description="desc",
            data=m.Data(
                assembly=[
                    m.Assembly2(
                        ngfirewall=m.NgFirewallDef(
                            entries=[
                                m.Entries(
                                    dst_zone=m.ZoneDef2(value="self", option_type="global"),
                                    src_zone=m.ZoneDef2(
                                        value="untrusted", option_type="global"
                                    ),
                                )
                            ],
                            ref_id=m.RefIdDef(value=ngfw_id, option_type="global"),
                        )
                    )
                ]
            ),
        )

    # make some aliases
    esn_api = client.v1.feature_profile.sdwan.embedded_security
    ngfw_api = client.v1.feature_profile.sdwan.embedded_security.unified.ngfirewall
    po_api = client.v1.feature_profile.sdwan.embedded_security.policy
    pg_api = client.v1.policy_group

    # create embedded security feature profile
    es_item = esn_api.create_sdwan_embedded_security_feature_profile(
        esn_api.m.EmbeddedSecurityDefault(name="psm-test", description="psm-descr")
    )

    # build and create ngfirewall
    ngfw_parcel = build_ngfw_parcel(ngfw_api.m)
    pf = ngfw_api.create_ngfirewall_profile_parcel(es_item.id, ngfw_parcel)

    # build and create embedded security policy
    policy = build_security_policy(po_api.m, pf.parcel_id)
    po_api.create_embedded_security_profile_parcel(es_item.id, policy)
    
    # build policy model
    model = pg_api.m.PolicyGroupDefault(
        name="psm-policy-group", description="descr", solution="sdwan"
    )

    # crate policy group
    policy_group_id = pg_api.create_policy_group(model).id

    # assing embedded security feature profile to policy group
    model.profiles = [
        pg_api.m.ProfileIdObjDef(id=es_item.id)
    ]
    pg_api.edit_policy_group(policy_group_id, model)
    
    # remove policy group
    pg_api.delete_policy_group(policy_group_id)

    # delete embedded security feature profile
    esn_api.delete_sdwan_embedded_security_feature_profile(es_item.id)



