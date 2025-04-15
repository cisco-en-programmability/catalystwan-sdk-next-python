=================================
v1.feature_profile.sd_routing.cli
=================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/cli
--------------------------------------------------------------


Create a SD-Routing CLI Feature Profile

.. code:: python

    def post(
        payload: CreateSdroutingCliFeatureProfilePostRequest,
    ) -> CreateSdroutingCliFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.sd_routing.cli.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/cli/{cliId}
---------------------------------------------------------------------


Edit a SD-Routing CLI Feature Profile

.. code:: python

    def put(
        cli_id: str, payload: EditSdroutingCliFeatureProfilePutRequest
    ) -> EditSdroutingCliFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.sd_routing.cli.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/cli/{cliId}
------------------------------------------------------------------------


Delete a SD-Routing CLI Feature Profile

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
        client.v1.feature_profile.sd_routing.cli.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli
-------------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> List[GetSdroutingCliFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.sd_routing.cli.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/cli/{cliId}
---------------------------------------------------------------------


.. code:: python

    @overload
    def get(cli_id: str) -> GetSingleSdRoutingCliPayload: ...


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
        client.v1.feature_profile.sd_routing.cli.get()


.. toctree::
    :maxdepth: 1

    features/index
    config/index
    full_config/index
    ios_config/index
    models

