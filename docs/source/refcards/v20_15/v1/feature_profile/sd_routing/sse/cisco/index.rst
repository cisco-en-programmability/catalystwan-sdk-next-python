=======================================
v1.feature_profile.sd_routing.sse.cisco
=======================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/sse/{sseId}/cisco
----------------------------------------------------------------------------


Create Cisco Sse feature for sse feature profile type

.. code:: python

    def post(
        sse_id: str, payload: CreateCiscoSseFeatureForSsePostRequest
    ) -> CreateCiscoSseFeatureForSsePostResponse: ...


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
        client.v1.feature_profile.sd_routing.sse.cisco.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/sse/{sseId}/cisco/{ciscoSseId}
----------------------------------------------------------------------------------------


Update a Cisco Sse feature

.. code:: python

    def put(
        sse_id: str,
        cisco_sse_id: str,
        payload: EditCiscoSseFeaturePutRequest,
    ) -> EditCiscoSseFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.sse.cisco.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/sse/{sseId}/cisco/{ciscoSseId}
-------------------------------------------------------------------------------------------


Delete a Cisco Sse Feature

.. code:: python

    def delete(sse_id: str, cisco_sse_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.sse.cisco.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/sse/{sseId}/cisco
---------------------------------------------------------------------------


.. code:: python

    @overload
    def get(sse_id: str) -> GetListSdRoutingSseCiscoSsePayload: ...


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
        client.v1.feature_profile.sd_routing.sse.cisco.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/sse/{sseId}/cisco/{ciscoSseId}
----------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        sse_id: str, cisco_sse_id: str
    ) -> GetSingleSdRoutingSseCiscoSsePayload: ...


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
        client.v1.feature_profile.sd_routing.sse.cisco.get()


.. toctree::
    :maxdepth: 1

    models

