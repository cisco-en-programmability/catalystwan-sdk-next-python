=============================================
v1.feature_profile.sd_routing.cli.full_config
=============================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/full-config
---------------------------------------------------------------------------------


Get the CLI Configuration by CLI profile ID

.. code:: python

    def get_sdrouting_cli_config_group_features(cli_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.cli.full_config.get_sdrouting_cli_config_group_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/full-config
----------------------------------------------------------------------------------


Create a SD-Routing CLI Configuration Group

.. code:: python

    def create_sdrouting_cli_config_group_feature(
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
        client.v1.feature_profile.sd_routing.cli.full_config.create_sdrouting_cli_config_group_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/full-config/{fullConfigId}
------------------------------------------------------------------------------------------------


Get the CLI Configuration by CLI profile ID and Config Feature ID

.. code:: python

    def get_sdrouting_cli_config_group_feature(
        cli_id: str, full_config_id: str
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
        client.v1.feature_profile.sd_routing.cli.full_config.get_sdrouting_cli_config_group_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/full-config/{fullConfigId}
------------------------------------------------------------------------------------------------


Edit a SD-Routing CLI Configuration Group

.. code:: python

    def edit_sdrouting_cli_config_group_feature(
        cli_id: str, full_config_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.cli.full_config.edit_sdrouting_cli_config_group_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/full-config/{fullConfigId}
---------------------------------------------------------------------------------------------------


Delete a SD-Routing CLI Configuration Group

.. code:: python

    def delete_sdrouting_cli_config_group_feature(
        cli_id: str, full_config_id: str
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
        client.v1.feature_profile.sd_routing.cli.full_config.delete_sdrouting_cli_config_group_feature()


