===================================
v1.feature_profile.mobility.global_
===================================


Operation: GET /dataservice/v1/feature-profile/mobility/global
--------------------------------------------------------------


Get Mobility Global Feature Profiles

.. code:: python

    def get_mobility_global_feature_profile(
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        reference_count: Optional[bool] = False,
    ) -> Any: ...


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
        client.v1.feature_profile.mobility.global_.get_mobility_global_feature_profile()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{globalId}
-------------------------------------------------------------------------


Get a Mobility Global Feature Profile by profileId

.. code:: python

    def get_mobility_feature_profile_by_global_id(
        global_id: str,
    ) -> Any: ...


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
        client.v1.feature_profile.mobility.global_.get_mobility_feature_profile_by_global_id()


.. toctree::
    :maxdepth: 1

    basic/index
    qos
    aaaservers
    cellular/index
    esimcellular
    ethernet/index
    logging
    network_protocol/index
    security_policy/index
    vpn
    wifi/index

