==============================================================
v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv6
==============================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv6
-----------------------------------------------------------------------------------------------------------------


Associate a WAN VPN parcel with a routing OSPFv3 parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_id: str,
        payload: CreateWanVpnAndRoutingOspfv3Ipv6AfParcelAssociationForTransportPostRequest,
    ) -> CreateWanVpnAndRoutingOspfv3Ipv6AfParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv6.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv6/{ospfv3Id}
---------------------------------------------------------------------------------------------------------------------------


Update a WAN VPN parcel and a routing OSPFv3 parcel association for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        ospfv3_id: str,
        payload: EditWanVpnAndRoutingOspfv3IPv6AfParcelAssociationForTransportPutRequest,
    ) -> EditWanVpnAndRoutingOspfv3IPv6AfParcelAssociationForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv6.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv6/{ospfv3Id}
------------------------------------------------------------------------------------------------------------------------------


Delete a WAN VPN parcel and a routing OSPFv3 parcel association for transport feature profile

.. code:: python

    def delete(
        transport_id: str, vpn_id: str, ospfv3_id: str
    ) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv6.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv6
----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str
    ) -> List[
        GetWanVpnAssociatedRoutingOspfv3IPv6AfParcelsForTransportGetResponse
    ]: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv6.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv6/{ospfv3Id}
---------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, ospfv3_id: str
    ) -> GetSingleSdwanTransportWanVpnRoutingOspfv3Ipv6Payload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv6.get()


.. toctree::
    :maxdepth: 1

    models

