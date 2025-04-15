======================================================
v1.feature_profile.sdwan.transport.routing.ospfv3.ipv6
======================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv6
-------------------------------------------------------------------------------------------------


Create a routing OSPFv3 IPv6 address family profile parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateRoutingOspfv3Ipv6AfProfileParcelForTransportPostRequest,
    ) -> (
        CreateRoutingOspfv3Ipv6AfProfileParcelForTransportPostResponse
    ): ...


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
        client.v1.feature_profile.sdwan.transport.routing.ospfv3.ipv6.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv6/{ospfv3Id}
-----------------------------------------------------------------------------------------------------------


Update a routing OSPFv3 IPv6 address family profile parcel for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        ospfv3_id: str,
        payload: EditRoutingOspfv3Ipv6AfProfileParcelForTransportPutRequest,
    ) -> EditRoutingOspfv3Ipv6AfProfileParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.routing.ospfv3.ipv6.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv6/{ospfv3Id}
--------------------------------------------------------------------------------------------------------------


Delete the routing OSPFv3 IPv6 address family profile parcel by ID for transport feature profile

.. code:: python

    def delete(transport_id: str, ospfv3_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.routing.ospfv3.ipv6.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv6
------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdwanTransportRoutingOspfv3Ipv6Payload: ...


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
        client.v1.feature_profile.sdwan.transport.routing.ospfv3.ipv6.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospfv3/ipv6/{ospfv3Id}
-----------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, ospfv3_id: str
    ) -> GetSingleSdwanTransportRoutingOspfv3Ipv6Payload: ...


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
        client.v1.feature_profile.sdwan.transport.routing.ospfv3.ipv6.get()


.. toctree::
    :maxdepth: 1

    models

