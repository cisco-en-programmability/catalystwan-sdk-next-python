======================================================
v1.feature_profile.sdwan.transport.wan.vpn.routing.bgp
======================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/bgp
--------------------------------------------------------------------------------------------------------


Get WanVpn associated Routing Bgp Parcels for transport feature profile

.. code:: python

    def get_wan_vpn_associated_routing_bgp_parcels_for_transport(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.bgp.get_wan_vpn_associated_routing_bgp_parcels_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/bgp
---------------------------------------------------------------------------------------------------------


Associate a wanvpn parcel with a routingbgp Parcel for transport feature profile

.. code:: python

    def create_wan_vpn_and_routing_bgp_parcel_association_for_transport(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.bgp.create_wan_vpn_and_routing_bgp_parcel_association_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/bgp/{bgpId}
----------------------------------------------------------------------------------------------------------------


Get WanVpn parcel associated RoutingBgp Parcel by bgpId for transport feature profile

.. code:: python

    def get_wan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_transport(
        transport_id: str, vpn_id: str, bgp_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.bgp.get_wan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/bgp/{bgpId}
----------------------------------------------------------------------------------------------------------------


Update a WanVpn parcel and a RoutingBgp Parcel association for transport feature profile

.. code:: python

    def edit_wan_vpn_and_routing_bgp_parcel_association_for_transport(
        transport_id: str,
        vpn_id: str,
        bgp_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.bgp.edit_wan_vpn_and_routing_bgp_parcel_association_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/bgp/{bgpId}
-------------------------------------------------------------------------------------------------------------------


Delete a WanVpn parcel and a RoutingBgp Parcel association for transport feature profile

.. code:: python

    def delete_wan_vpn_and_routing_bgp_association_for_transport(
        transport_id: str, vpn_id: str, bgp_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.bgp.delete_wan_vpn_and_routing_bgp_association_for_transport()


