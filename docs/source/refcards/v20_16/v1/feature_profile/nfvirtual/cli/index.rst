================================
v1.feature_profile.nfvirtual.cli
================================


Operation: GET /dataservice/v1/feature-profile/nfvirtual/cli
------------------------------------------------------------


Get all Nfvirtual CLI Feature Profiles

.. code:: python

    def get_all_nfvirtual_cli_feature_profiles(
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
        client.v1.feature_profile.nfvirtual.cli.get_all_nfvirtual_cli_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/nfvirtual/cli
-------------------------------------------------------------


Create a Nfvirtual CLI Feature Profile

.. code:: python

    def create_nfvirtual_cli_feature_profile(
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
        client.v1.feature_profile.nfvirtual.cli.create_nfvirtual_cli_feature_profile()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/cli/{cliId}
--------------------------------------------------------------------


Get nfvirtual CLI Feature Profile with cliId

.. code:: python

    def get_nfvirtual_cli_feature_profile_byid(cli_id: str) -> Any: ...


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
        client.v1.feature_profile.nfvirtual.cli.get_nfvirtual_cli_feature_profile_byid()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/cli/{cliId}
--------------------------------------------------------------------


Edit a Nfvirtual CLI Feature Profile

.. code:: python

    def edit_nfvirtual_cli_feature_profile(
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
        client.v1.feature_profile.nfvirtual.cli.edit_nfvirtual_cli_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/cli/{cliId}
-----------------------------------------------------------------------


Delete nfvirtual CLI Feature Profile

.. code:: python

    def delete_nfvirtual_cli_feature_profile(cli_id: str) -> None: ...


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
        client.v1.feature_profile.nfvirtual.cli.delete_nfvirtual_cli_feature_profile()


.. toctree::
    :maxdepth: 1

    config

