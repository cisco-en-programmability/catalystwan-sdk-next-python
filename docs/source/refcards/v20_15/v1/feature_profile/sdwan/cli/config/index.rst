===================================
v1.feature_profile.sdwan.cli.config
===================================


Operation: POST /dataservice/v1/feature-profile/sdwan/cli/{cliId}/config
------------------------------------------------------------------------


Create a config Profile Parcel for cli feature profile

.. code:: python

    def post(
        cli_id: str,
        payload: CreateSdwanConfigProfileParcelForCliPostRequest,
    ) -> CreateSdwanConfigProfileParcelForCliPostResponse: ...


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
        client.v1.feature_profile.sdwan.cli.config.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/cli/{cliId}/config/{configId}
----------------------------------------------------------------------------------


Update a config Profile Parcel for cli feature profile

.. code:: python

    def put(
        cli_id: str,
        config_id: str,
        payload: EditConfigProfileParcelForCliPutRequest,
    ) -> EditConfigProfileParcelForCliPutResponse: ...


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
        client.v1.feature_profile.sdwan.cli.config.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/cli/{cliId}/config/{configId}
-------------------------------------------------------------------------------------


Delete a config Profile Parcel for cli feature profile

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
        client.v1.feature_profile.sdwan.cli.config.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/cli/{cliId}/config
-----------------------------------------------------------------------


.. code:: python

    @overload
    def get(cli_id: str) -> GetListSdwanCliConfigPayload: ...


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
        client.v1.feature_profile.sdwan.cli.config.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/cli/{cliId}/config/{configId}
----------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        cli_id: str, config_id: str
    ) -> GetSingleSdwanCliConfigPayload: ...


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
        client.v1.feature_profile.sdwan.cli.config.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

