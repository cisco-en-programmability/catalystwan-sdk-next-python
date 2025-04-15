========================================
v1.feature_profile.sd_routing.cli.config
========================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/config
-----------------------------------------------------------------------------


Create a SD-Routing CLI Add-On Feature for CLI Feature Profile

.. code:: python

    def post(
        cli_id: str, payload: CreateSdroutingCliAddOnFeaturePostRequest
    ) -> CreateSdroutingCliAddOnFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.cli.config.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/config/{configId}
---------------------------------------------------------------------------------------


Edit a SD-Routing CLI Add-On Feature for CLI Feature Profile

.. code:: python

    def put(
        cli_id: str,
        config_id: str,
        payload: EditSdroutingCliAddOnFeaturePutRequest,
    ) -> EditSdroutingCliAddOnFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.cli.config.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/config/{configId}
------------------------------------------------------------------------------------------


Delete a SD-Routing CLI Add-On Feature for CLI Feature Profile

.. code:: python

    def delete(cli_id: str, config_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.cli.config.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/config
----------------------------------------------------------------------------


.. code:: python

    @overload
    def get(cli_id: str) -> GetListSdRoutingCliConfigPayload: ...


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
        client.v1.feature_profile.sd_routing.cli.config.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/config/{configId}
---------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        cli_id: str, config_id: str
    ) -> GetSingleSdRoutingCliConfigPayload: ...


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
        client.v1.feature_profile.sd_routing.cli.config.get()


.. toctree::
    :maxdepth: 1

    models

