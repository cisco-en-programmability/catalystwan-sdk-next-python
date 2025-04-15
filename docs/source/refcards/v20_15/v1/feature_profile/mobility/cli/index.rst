===============================
v1.feature_profile.mobility.cli
===============================


Operation: GET /dataservice/v1/feature-profile/mobility/cli
-----------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        reference_count: Optional[bool] = False,
    ) -> List[GetMobilityCliFeatureProfileGetResponse]: ...


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
        client.v1.feature_profile.mobility.cli.get()


Operation: GET /dataservice/v1/feature-profile/mobility/cli/{cliId}
-------------------------------------------------------------------


.. code:: python

    @overload
    def get(cli_id: str) -> GetSingleMobilityCliPayload: ...


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
        client.v1.feature_profile.mobility.cli.get()


.. toctree::
    :maxdepth: 1

    config/index
    models

