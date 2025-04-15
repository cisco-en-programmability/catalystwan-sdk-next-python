=======================================
v1.feature_profile.nfvirtual.cli.config
=======================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/cli/{cliId}/config
----------------------------------------------------------------------------


Create CLI Profile Parcel for CLI feature profile

.. code:: python

    def post(
        cli_id: str, payload: CreateNfvirtualCliParcelPostRequest
    ) -> CreateNfvirtualCliParcelPostResponse: ...


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
        client.v1.feature_profile.nfvirtual.cli.config.post()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/cli/{cliId}/config/{configId}
--------------------------------------------------------------------------------------


Get CLI Profile Parcels for CLI feature profile

.. code:: python

    def get(
        cli_id: str, config_id: str
    ) -> GetSingleNfvirtualCliConfigPayload: ...


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
        client.v1.feature_profile.nfvirtual.cli.config.get()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/cli/{cliId}/config/{configId}
--------------------------------------------------------------------------------------


Edit CLI Profile Parcel for CLI feature profile

.. code:: python

    def put(
        cli_id: str,
        config_id: str,
        payload: EditNfvirtualCliParcelPutRequest,
    ) -> EditNfvirtualCliParcelPutResponse: ...


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
        client.v1.feature_profile.nfvirtual.cli.config.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/cli/{cliId}/config/{configId}
-----------------------------------------------------------------------------------------


Delete CLI Profile Parcel for CLI feature profile

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
        client.v1.feature_profile.nfvirtual.cli.config.delete()


.. toctree::
    :maxdepth: 1

    models

