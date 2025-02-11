=======================================
v1.feature_profile.nfvirtual.cli.config
=======================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/cli/{cliId}/config
----------------------------------------------------------------------------


Create CLI Profile Parcel for CLI feature profile

.. code:: python

    def create_nfvirtual_cli_parcel(
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
        client.v1.feature_profile.nfvirtual.cli.config.create_nfvirtual_cli_parcel()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/cli/{cliId}/config/{configId}
--------------------------------------------------------------------------------------


Get CLI Profile Parcels for CLI feature profile

.. code:: python

    def get_nfvirtual_cli_parcel(cli_id: str, config_id: str) -> str: ...


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
        client.v1.feature_profile.nfvirtual.cli.config.get_nfvirtual_cli_parcel()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/cli/{cliId}/config/{configId}
--------------------------------------------------------------------------------------


Edit CLI Profile Parcel for CLI feature profile

.. code:: python

    def edit_nfvirtual_cli_parcel(
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
        client.v1.feature_profile.nfvirtual.cli.config.edit_nfvirtual_cli_parcel()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/cli/{cliId}/config/{configId}
-----------------------------------------------------------------------------------------


Delete CLI Profile Parcel for CLI feature profile

.. code:: python

    def delete_nfvirtual_cli_parcel(
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
        client.v1.feature_profile.nfvirtual.cli.config.delete_nfvirtual_cli_parcel()


