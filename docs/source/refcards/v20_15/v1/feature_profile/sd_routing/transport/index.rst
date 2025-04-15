=======================================
v1.feature_profile.sd_routing.transport
=======================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport
--------------------------------------------------------------------


Create a SD-Routing Transport Feature Profile

.. code:: python

    def post(
        payload: CreateSdroutingTransportFeatureProfilePostRequest,
    ) -> CreateSdroutingTransportFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}
---------------------------------------------------------------------------------


Edit a SD-Routing Transport Feature Profile

.. code:: python

    def put(
        transport_id: str,
        payload: EditSdroutingTransportFeatureProfilePutRequest,
    ) -> EditSdroutingTransportFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}
------------------------------------------------------------------------------------


Delete a SD-Routing Transport Feature Profile

.. code:: python

    def delete(transport_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.transport.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport
-------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> List[GetSdroutingTransportFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.sd_routing.transport.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}
---------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(transport_id: str) -> GetSingleSdRoutingTransportPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.get()


.. toctree::
    :maxdepth: 1

    global_vrf/index
    ipv4_acl/index
    management_vrf/index
    multicloud_connection/index
    objecttracker/index
    objecttrackergroup/index
    route_policy/index
    routing/index
    vrf/index
    models

