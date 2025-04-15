=============================================
v1.feature_profile.sd_routing.cli.full_config
=============================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/full-config
----------------------------------------------------------------------------------


Create a SD-Routing CLI Configuration Group

.. code:: python

    def post(
        cli_id: str,
        payload: CreateSdroutingCliConfigGroupFeaturePostRequest,
    ) -> CreateSdroutingCliConfigGroupFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.cli.full_config.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/full-config/{fullConfigId}
------------------------------------------------------------------------------------------------


Edit a SD-Routing CLI Configuration Group

.. code:: python

    def put(
        cli_id: str,
        full_config_id: str,
        payload: EditSdroutingCliConfigGroupFeaturePutRequest,
    ) -> EditSdroutingCliConfigGroupFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.cli.full_config.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/full-config/{fullConfigId}
---------------------------------------------------------------------------------------------------


Delete a SD-Routing CLI Configuration Group

.. code:: python

    def delete(cli_id: str, full_config_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.cli.full_config.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/full-config
---------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(cli_id: str) -> GetListSdRoutingCliFullConfigPayload: ...


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
        client.v1.feature_profile.sd_routing.cli.full_config.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli/{cliId}/full-config/{fullConfigId}
------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        cli_id: str, full_config_id: str
    ) -> GetSingleSdRoutingCliFullConfigPayload: ...


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
        client.v1.feature_profile.sd_routing.cli.full_config.get()


.. toctree::
    :maxdepth: 1

    models

