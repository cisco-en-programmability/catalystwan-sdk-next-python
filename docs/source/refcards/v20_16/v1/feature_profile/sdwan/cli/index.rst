============================
v1.feature_profile.sdwan.cli
============================


Operation: GET /dataservice/v1/feature-profile/sdwan/cli
--------------------------------------------------------


Get all SDWAN Feature Profiles with giving Family and profile type

.. code:: python

    def get_sdwan_feature_profiles_by_family_and_type_1(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> Any: ...


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
        client.v1.feature_profile.sdwan.cli.get_sdwan_feature_profiles_by_family_and_type_1()


Operation: POST /dataservice/v1/feature-profile/sdwan/cli
---------------------------------------------------------


Create a SDWAN  Feature Profile with profile type

.. code:: python

    def create_sdwan_feature_profile(
        payload: Optional[str] = None,
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
        client.v1.feature_profile.sdwan.cli.create_sdwan_feature_profile()


Operation: GET /dataservice/v1/feature-profile/sdwan/cli/{cliId}
----------------------------------------------------------------


Get a SDWAN Feature Profile with Cli profile type

.. code:: python

    def get_sdwan_feature_profile_by_profile_id(cli_id: str) -> Any: ...


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
        client.v1.feature_profile.sdwan.cli.get_sdwan_feature_profile_by_profile_id()


Operation: PUT /dataservice/v1/feature-profile/sdwan/cli/{cliId}
----------------------------------------------------------------


Edit a SDWAN Feature Profile

.. code:: python

    def edit_sdwan_feature_profile(
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
        client.v1.feature_profile.sdwan.cli.edit_sdwan_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/cli/{cliId}
-------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete_sdwan_feature_profile_for_cli(cli_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.cli.delete_sdwan_feature_profile_for_cli()


.. toctree::
    :maxdepth: 1

    config/index
    features

