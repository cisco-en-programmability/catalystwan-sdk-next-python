============================
v1.feature_profile.sdwan.cli
============================


Operation: POST /dataservice/v1/feature-profile/sdwan/cli
---------------------------------------------------------


Create a SDWAN  Feature Profile with profile type

.. code:: python

    def post(
        payload: CreateSdwanFeatureProfilePostRequest,
    ) -> CreateSdwanFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.sdwan.cli.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/cli/{cliId}
----------------------------------------------------------------


Edit a SDWAN Feature Profile

.. code:: python

    def put(
        cli_id: str, payload: EditSdwanFeatureProfilePutRequest
    ) -> EditSdwanFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.sdwan.cli.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/cli/{cliId}
-------------------------------------------------------------------


Delete Feature Profile

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
        client.v1.feature_profile.sdwan.cli.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/cli
--------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> List[GetSdwanFeatureProfilesByFamilyAndTypeGetResponse]: ...


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
        client.v1.feature_profile.sdwan.cli.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/cli/{cliId}
----------------------------------------------------------------


.. code:: python

    @overload
    def get(cli_id: str) -> GetSingleSdwanCliPayload: ...


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
        client.v1.feature_profile.sdwan.cli.get()


.. toctree::
    :maxdepth: 1

    config/index
    features/index
    models

