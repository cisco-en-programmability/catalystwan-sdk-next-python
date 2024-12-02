==============================================================
v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv4
==============================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4
----------------------------------------------------------------------------------------------------------------


Get WAN VPN associated routing OSPFv3 IPv4 address family parcels for transport feature profile

.. code:: python

    def get_wan_vpn_associated_routing_ospfv3_i_pv4_af_parcels_for_transport(
        transport_id: str, vpn_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv4.get_wan_vpn_associated_routing_ospfv3_i_pv4_af_parcels_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4
-----------------------------------------------------------------------------------------------------------------


Associate a WAN VPN parcel with a routing OSPFv3 parcel for transport feature profile

.. code:: python

    def create_wan_vpn_and_routing_ospfv3_ipv4_af_parcel_association_for_transport(
        transport_id: str, vpn_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv4.create_wan_vpn_and_routing_ospfv3_ipv4_af_parcel_association_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4/{ospfv3Id}
---------------------------------------------------------------------------------------------------------------------------


Get WAN VPN parcel associated OSPFv3 IPv4 parcel by ID for transport feature profile

.. code:: python

    def get_wan_vpn_associated_routing_ospfv3_i_pv4_af_parcel_by_parcel_id_for_transport(
        transport_id: str, vpn_id: str, ospfv3_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv4.get_wan_vpn_associated_routing_ospfv3_i_pv4_af_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4/{ospfv3Id}
---------------------------------------------------------------------------------------------------------------------------


Update a WAN VPN parcel and a routing OSPFv3 parcel association for transport feature profile

.. code:: python

    def edit_wan_vpn_and_routing_ospfv3_i_pv4_af_parcel_association_for_transport(
        transport_id: str,
        vpn_id: str,
        ospfv3_id: str,
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv4.edit_wan_vpn_and_routing_ospfv3_i_pv4_af_parcel_association_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospfv3/ipv4/{ospfv3Id}
------------------------------------------------------------------------------------------------------------------------------


Delete a WAN VPN parcel and a routing OSPFv3 parcel association for transport feature profile

.. code:: python

    def delete_wan_vpn_and_routing_ospfv3_i_pv4_association_for_transport(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospfv3.ipv4.delete_wan_vpn_and_routing_ospfv3_i_pv4_association_for_transport()


