==============================================================
v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv4
==============================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4
-----------------------------------------------------------------------------------------------------------------


Associate a WAN VPN parcel with a routing OSPFv3 parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_id: str,
        payload: CreateWanVpnAndRoutingOspfv3Ipv4AfParcelAssociationForTransportPostRequest,
    ) -> CreateWanVpnAndRoutingOspfv3Ipv4AfParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv4.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4/{ospfv3Id}
---------------------------------------------------------------------------------------------------------------------------


Update a WAN VPN parcel and a routing OSPFv3 parcel association for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        ospfv3_id: str,
        payload: EditWanVpnAndRoutingOspfv3IPv4AfParcelAssociationForTransportPutRequest,
    ) -> EditWanVpnAndRoutingOspfv3IPv4AfParcelAssociationForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv4.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4/{ospfv3Id}
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv4.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4
----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str
    ) -> List[
        GetWanVpnAssociatedRoutingOspfv3IPv4AfParcelsForTransportGetResponse
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv4.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4/{ospfv3Id}
---------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, ospfv3_id: str
    ) -> GetSingleSdwanTransportWanVpnRoutingOspfv3Ipv4Payload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv4.get()


.. toctree::
    :maxdepth: 1

    models

