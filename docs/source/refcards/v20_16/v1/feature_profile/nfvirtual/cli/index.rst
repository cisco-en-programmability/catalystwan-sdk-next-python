================================
v1.feature_profile.nfvirtual.cli
================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/cli
-------------------------------------------------------------


Create a Nfvirtual CLI Feature Profile

.. code:: python

    def post(
        payload: CreateNfvirtualCliFeatureProfilePostRequest,
    ) -> CreateNfvirtualCliFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.nfvirtual.cli.post()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/cli/{cliId}
--------------------------------------------------------------------


Edit a Nfvirtual CLI Feature Profile

.. code:: python

    def put(
        cli_id: str, payload: EditNfvirtualCliFeatureProfilePutRequest
    ) -> EditNfvirtualCliFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.nfvirtual.cli.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/cli/{cliId}
-----------------------------------------------------------------------


Delete nfvirtual CLI Feature Profile

.. code:: python

    def delete(cli_id: str) -> None: ...


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
        client.v1.feature_profile.nfvirtual.cli.delete()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/cli
------------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> List[GetAllNfvirtualCliFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.nfvirtual.cli.get()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/cli/{cliId}
--------------------------------------------------------------------


.. code:: python

    @overload
    def get(cli_id: str) -> GetSingleNfvirtualCliPayload: ...


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
        client.v1.feature_profile.nfvirtual.cli.get()


.. toctree::
    :maxdepth: 1

    config/index
    models

