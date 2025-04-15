===================================
v1.feature_profile.mobility.global_
===================================


Operation: GET /dataservice/v1/feature-profile/mobility/global
--------------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        reference_count: Optional[bool] = False,
    ) -> List[GetMobilityGlobalFeatureProfileGetResponse]: ...


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
        client.v1.feature_profile.mobility.global_.get()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{globalId}
-------------------------------------------------------------------------


.. code:: python

    @overload
    def get(global_id: str) -> GetSingleMobilityGlobalPayload: ...


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
        client.v1.feature_profile.mobility.global_.get()


.. toctree::
    :maxdepth: 1

    basic/index
    qos/index
    aaaservers/index
    cellular/index
    esimcellular/index
    ethernet/index
    logging/index
    network_protocol/index
    security_policy/index
    vpn/index
    wifi/index
    models

