============================================
v1.feature_profile.sd_routing.cli.ios_config
============================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/ios-config
--------------------------------------------------------------------------------


SD-Routing Ios Classic CLI Add-On Features for CLI Feature Profile for GET requests

.. code:: python

    def get_sdrouting_ios_c_lassic_cli_add_on_features(
        cli_id: str,
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
        client.v1.feature_profile.sd_routing.cli.ios_config.get_sdrouting_ios_c_lassic_cli_add_on_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/ios-config
---------------------------------------------------------------------------------


SD-Routing Ios Classic CLI Add-On Feature for CLI Feature Profile for POST requests

.. code:: python

    def create_sdrouting_ios_classic_cli_add_on_feature(
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
        client.v1.feature_profile.sd_routing.cli.ios_config.create_sdrouting_ios_classic_cli_add_on_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/ios-config/{iosConfigId}
----------------------------------------------------------------------------------------------


SD-Routing Ios Classic CLI Add-On Feature for CLI Feature Profile for GET requests

.. code:: python

    def get_sdrouting_ios_classic_cli_add_on_feature(
        cli_id: str, ios_config_id: str
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
        client.v1.feature_profile.sd_routing.cli.ios_config.get_sdrouting_ios_classic_cli_add_on_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/ios-config/{iosConfigId}
----------------------------------------------------------------------------------------------


SD-Routing Ios Classic CLI Add-On Feature for CLI Feature Profile for PUT requests

.. code:: python

    def edit_sdrouting_ios_classic_cli_add_on_feature(
        cli_id: str, ios_config_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.cli.ios_config.edit_sdrouting_ios_classic_cli_add_on_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/ios-config/{iosConfigId}
-------------------------------------------------------------------------------------------------


Delete a SD-Routing Ios Classic CLI Add-On Feature for CLI Feature Profile

.. code:: python

    def delete_sdrouting_ios_classic_cli_add_on_feature(
        cli_id: str, ios_config_id: str
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
        client.v1.feature_profile.sd_routing.cli.ios_config.delete_sdrouting_ios_classic_cli_add_on_feature()


