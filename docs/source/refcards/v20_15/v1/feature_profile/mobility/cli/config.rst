======================================
v1.feature_profile.mobility.cli.config
======================================


Operation: GET /dataservice/v1/feature-profile/mobility/cli/{cliId}/config
--------------------------------------------------------------------------


Get config Features for cli feature profile

.. code:: python

    def get_all_config_feature_for_mobility(cli_id: str) -> str: ...


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
        client.v1.feature_profile.mobility.cli.config.get_all_config_feature_for_mobility()


Operation: POST /dataservice/v1/feature-profile/mobility/cli/{cliId}/config
---------------------------------------------------------------------------


Create a config Feature for cli feature profile

.. code:: python

    def create_config_feature_for_mobility(
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
        client.v1.feature_profile.mobility.cli.config.create_config_feature_for_mobility()


Operation: GET /dataservice/v1/feature-profile/mobility/cli/{cliId}/config/{configId}
-------------------------------------------------------------------------------------


Get config Feature by configId for cli feature profile

.. code:: python

    def get_config_feature_for_mobility_by_parcel_id(
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
        client.v1.feature_profile.mobility.cli.config.get_config_feature_for_mobility_by_parcel_id()


Operation: PUT /dataservice/v1/feature-profile/mobility/cli/{cliId}/config/{configId}
-------------------------------------------------------------------------------------


Update a config Feature for cli feature profile

.. code:: python

    def edit_config_feature_for_mobility(
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
        client.v1.feature_profile.mobility.cli.config.edit_config_feature_for_mobility()


Operation: DELETE /dataservice/v1/feature-profile/mobility/cli/{cliId}/config/{configId}
----------------------------------------------------------------------------------------


Delete a config Feature for cli feature profile

.. code:: python

    def delete_config_feature_for_mobility(
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
        client.v1.feature_profile.mobility.cli.config.delete_config_feature_for_mobility()


