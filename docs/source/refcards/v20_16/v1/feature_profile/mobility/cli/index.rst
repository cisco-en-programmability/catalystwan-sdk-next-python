===============================
v1.feature_profile.mobility.cli
===============================


Operation: GET /dataservice/v1/feature-profile/mobility/cli
-----------------------------------------------------------


Get Mobility Cli Feature Profiles

.. code:: python

    def get_mobility_cli_feature_profile(
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
        client.v1.feature_profile.mobility.cli.get_mobility_cli_feature_profile()


Operation: GET /dataservice/v1/feature-profile/mobility/cli/{cliId}
-------------------------------------------------------------------


Get a Mobility Feature Profile with Cli profile type

.. code:: python

    def get_mobility_cli_feature_profile_by_cli_id(
        cli_id: str,
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
        client.v1.feature_profile.mobility.cli.get_mobility_cli_feature_profile_by_cli_id()


.. toctree::
    :maxdepth: 1

    config

