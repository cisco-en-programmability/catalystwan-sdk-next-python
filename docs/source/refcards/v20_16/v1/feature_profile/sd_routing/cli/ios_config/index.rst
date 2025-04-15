============================================
v1.feature_profile.sd_routing.cli.ios_config
============================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/ios-config
---------------------------------------------------------------------------------


SD-Routing Ios Classic CLI Add-On Feature for CLI Feature Profile for POST requests

.. code:: python

    def post(
        cli_id: str,
        payload: CreateSdroutingIosClassicCliAddOnFeaturePostRequest,
    ) -> CreateSdroutingIosClassicCliAddOnFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.cli.ios_config.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/ios-config/{iosConfigId}
----------------------------------------------------------------------------------------------


SD-Routing Ios Classic CLI Add-On Feature for CLI Feature Profile for PUT requests

.. code:: python

    def put(
        cli_id: str,
        ios_config_id: str,
        payload: EditSdroutingIosClassicCliAddOnFeaturePutRequest,
    ) -> EditSdroutingIosClassicCliAddOnFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.cli.ios_config.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/ios-config/{iosConfigId}
-------------------------------------------------------------------------------------------------


Delete a SD-Routing Ios Classic CLI Add-On Feature for CLI Feature Profile

.. code:: python

    def delete(cli_id: str, ios_config_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.cli.ios_config.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/ios-config
--------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(cli_id: str) -> GetListSdRoutingCliIosConfigPayload: ...


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
        client.v1.feature_profile.sd_routing.cli.ios_config.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/ios-config/{iosConfigId}
----------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        cli_id: str, ios_config_id: str
    ) -> GetSingleSdRoutingCliIosConfigPayload: ...


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
        client.v1.feature_profile.sd_routing.cli.ios_config.get()


.. toctree::
    :maxdepth: 1

    models

