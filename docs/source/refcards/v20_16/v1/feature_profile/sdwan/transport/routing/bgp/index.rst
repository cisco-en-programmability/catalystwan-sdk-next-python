==============================================
v1.feature_profile.sdwan.transport.routing.bgp
==============================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/bgp
-----------------------------------------------------------------------------------------


Create a Routing Bgp Profile Parcel for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateRoutingBgpProfileParcelForTransportPostRequest,
    ) -> CreateRoutingBgpProfileParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.routing.bgp.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/bgp/{bgpId}
------------------------------------------------------------------------------------------------


Update a Routing Bgp Profile Parcel for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        bgp_id: str,
        payload: EditRoutingBgpProfileParcelForTransportPutRequest,
    ) -> EditRoutingBgpProfileParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.routing.bgp.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/bgp/{bgpId}
---------------------------------------------------------------------------------------------------


Delete a Routing Bgp Profile Parcel for Transport feature profile

.. code:: python

    def delete(transport_id: str, bgp_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.routing.bgp.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/bgp
----------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdwanTransportRoutingBgpPayload: ...


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
        client.v1.feature_profile.sdwan.transport.routing.bgp.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/bgp/{bgpId}
------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, bgp_id: str
    ) -> GetSingleSdwanTransportRoutingBgpPayload: ...


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
        client.v1.feature_profile.sdwan.transport.routing.bgp.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

