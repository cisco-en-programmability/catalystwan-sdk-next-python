========================================
v1.feature_profile.sd_routing.cli.config
========================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/config
----------------------------------------------------------------------------


Get all SD-Routing CLI Add-On Features for CLI Feature Profile

.. code:: python

    def get_sdrouting_cli_add_on_features(cli_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.cli.config.get_sdrouting_cli_add_on_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/config
-----------------------------------------------------------------------------


Create a SD-Routing CLI Add-On Feature for CLI Feature Profile

.. code:: python

    def create_sdrouting_cli_add_on_feature(
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
        client.v1.feature_profile.sd_routing.cli.config.create_sdrouting_cli_add_on_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/config/{configId}
---------------------------------------------------------------------------------------


Get a SD-Routing CLI Add-On Feature for CLI Feature Profile

.. code:: python

    def get_sdrouting_cli_add_on_feature(
        cli_id: str, config_id: str
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
        client.v1.feature_profile.sd_routing.cli.config.get_sdrouting_cli_add_on_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/config/{configId}
---------------------------------------------------------------------------------------


Edit a SD-Routing CLI Add-On Feature for CLI Feature Profile

.. code:: python

    def edit_sdrouting_cli_add_on_feature(
        cli_id: str, config_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.cli.config.edit_sdrouting_cli_add_on_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/config/{configId}
------------------------------------------------------------------------------------------


Delete a SD-Routing CLI Add-On Feature for CLI Feature Profile

.. code:: python

    def delete_sdrouting_cli_add_on_feature(
        cli_id: str, config_id: str
    ) -> None: ...


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
        client.v1.feature_profile.sd_routing.cli.config.delete_sdrouting_cli_add_on_feature()


