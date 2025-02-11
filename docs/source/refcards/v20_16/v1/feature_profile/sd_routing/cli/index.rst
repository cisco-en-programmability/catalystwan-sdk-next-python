=================================
v1.feature_profile.sd_routing.cli
=================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli
-------------------------------------------------------------


Get all SD-Routing CLI Feature Profiles

.. code:: python

    def get_sdrouting_cli_feature_profiles(
        offset: Optional[int] = None, limit: Optional[int] = 0
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
        client.v1.feature_profile.sd_routing.cli.get_sdrouting_cli_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/sd-routing/cli
--------------------------------------------------------------


Create a SD-Routing CLI Feature Profile

.. code:: python

    def create_sdrouting_cli_feature_profile(
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.cli.create_sdrouting_cli_feature_profile()


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli/{cliId}
---------------------------------------------------------------------


Get a SD-Routing CLI Feature Profile

.. code:: python

    def get_sdrouting_cli_feature_profile(cli_id: str) -> Any: ...


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
        client.v1.feature_profile.sd_routing.cli.get_sdrouting_cli_feature_profile()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/cli/{cliId}
---------------------------------------------------------------------


Edit a SD-Routing CLI Feature Profile

.. code:: python

    def edit_sdrouting_cli_feature_profile(
        cli_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.cli.edit_sdrouting_cli_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/cli/{cliId}
------------------------------------------------------------------------


Delete a SD-Routing CLI Feature Profile

.. code:: python

    def delete_sdrouting_cli_feature_profile(cli_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.cli.delete_sdrouting_cli_feature_profile()


.. toctree::
    :maxdepth: 1

    features
    config
    full_config
    ios_config

