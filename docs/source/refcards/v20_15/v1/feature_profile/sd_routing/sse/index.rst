=================================
v1.feature_profile.sd_routing.sse
=================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/sse
--------------------------------------------------------------


Create a SD-ROUTING SSE Feature Profile

.. code:: python

    def post(
        payload: CreateSdRoutingSseFeatureProfilePostRequest,
    ) -> CreateSdRoutingSseFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.sd_routing.sse.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/sse/{sseId}
---------------------------------------------------------------------


Edit a SD-ROUTING SSE Feature Profile

.. code:: python

    def put(
        sse_id: str, payload: EditSdRoutingSseFeatureProfilePutRequest
    ) -> EditSdRoutingSseFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.sd_routing.sse.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/sse/{sseId}
------------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete(sse_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.sse.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/sse
-------------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        reference_count: Optional[bool] = False,
    ) -> List[GetSdRoutingSseFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.sd_routing.sse.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/sse/{sseId}
---------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        sse_id: str, references: Optional[bool] = False
    ) -> GetSingleSdRoutingSsePayload: ...


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
        client.v1.feature_profile.sd_routing.sse.get()


.. toctree::
    :maxdepth: 1

    cisco/index
    models

