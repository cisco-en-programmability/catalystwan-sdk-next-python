===================================
v1.feature_profile.sdwan.cli.config
===================================


Operation: GET /dataservice/v1/feature-profile/sdwan/cli/{cliId}/config
-----------------------------------------------------------------------


Get config Profile Parcels for cli feature profile

.. code:: python

    def get_config_profile_parcel_for_cli(cli_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.cli.config.get_config_profile_parcel_for_cli()


Operation: POST /dataservice/v1/feature-profile/sdwan/cli/{cliId}/config
------------------------------------------------------------------------


Create a config Profile Parcel for cli feature profile

.. code:: python

    def create_sdwan_config_profile_parcel_for_cli(
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
        client.v1.feature_profile.sdwan.cli.config.create_sdwan_config_profile_parcel_for_cli()


Operation: GET /dataservice/v1/feature-profile/sdwan/cli/{cliId}/config/{configId}
----------------------------------------------------------------------------------


Get config Profile Parcel by configId for cli feature profile

.. code:: python

    def get_config_profile_parcel_by_parcel_id_for_cli(
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
        client.v1.feature_profile.sdwan.cli.config.get_config_profile_parcel_by_parcel_id_for_cli()


Operation: PUT /dataservice/v1/feature-profile/sdwan/cli/{cliId}/config/{configId}
----------------------------------------------------------------------------------


Update a config Profile Parcel for cli feature profile

.. code:: python

    def edit_config_profile_parcel_for_cli(
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
        client.v1.feature_profile.sdwan.cli.config.edit_config_profile_parcel_for_cli()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/cli/{cliId}/config/{configId}
-------------------------------------------------------------------------------------


Delete a config Profile Parcel for cli feature profile

.. code:: python

    def delete_config_profile_parcel_for_cli(
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
        client.v1.feature_profile.sdwan.cli.config.delete_config_profile_parcel_for_cli()


.. toctree::
    :maxdepth: 1

    schema/index

