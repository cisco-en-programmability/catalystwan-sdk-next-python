======================================
v1.feature_profile.mobility.cli.config
======================================


Operation: POST /dataservice/v1/feature-profile/mobility/cli/{cliId}/config
---------------------------------------------------------------------------


Create a config Feature for cli feature profile

.. code:: python

    def post(
        cli_id: str, payload: CreateConfigFeatureForMobilityPostRequest
    ) -> CreateConfigFeatureForMobilityPostResponse: ...


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
        client.v1.feature_profile.mobility.cli.config.post()


Operation: PUT /dataservice/v1/feature-profile/mobility/cli/{cliId}/config/{configId}
-------------------------------------------------------------------------------------


Update a config Feature for cli feature profile

.. code:: python

    def put(
        cli_id: str,
        config_id: str,
        payload: EditConfigFeatureForMobilityPutRequest,
    ) -> EditConfigFeatureForMobilityPutResponse: ...


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
        client.v1.feature_profile.mobility.cli.config.put()


Operation: DELETE /dataservice/v1/feature-profile/mobility/cli/{cliId}/config/{configId}
----------------------------------------------------------------------------------------


Delete a config Feature for cli feature profile

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
        client.v1.feature_profile.mobility.cli.config.delete()


Operation: GET /dataservice/v1/feature-profile/mobility/cli/{cliId}/config
--------------------------------------------------------------------------


.. code:: python

    @overload
    def get(cli_id: str) -> GetListMobilityCliConfigPayload: ...


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
        client.v1.feature_profile.mobility.cli.config.get()


Operation: GET /dataservice/v1/feature-profile/mobility/cli/{cliId}/config/{configId}
-------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        cli_id: str, config_id: str
    ) -> GetSingleMobilityCliConfigPayload: ...


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
        client.v1.feature_profile.mobility.cli.config.get()


.. toctree::
    :maxdepth: 1

    models

