========================
v1.feature_profile.sdwan
========================


Operation: GET /dataservice/v1/feature-profile/sdwan
----------------------------------------------------


Get all SDWAN Feature Profiles

.. code:: python

    def get_sdwan_feature_profile_by_sdwan_family(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> List[GetSdwanFeatureProfileBySdwanFamilyGetResponse]: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.v1.feature_profile.sdwan.get_sdwan_feature_profile_by_sdwan_family()


.. toctree::
    :maxdepth: 1

    application_priority/index
    cli/index
    dns_security/index
    embedded_security/index
    other/index
    policy_object/index
    service/index
    sig_security/index
    system/index
    transport/index
    models

