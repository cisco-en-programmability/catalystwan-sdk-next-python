=======================================================
v1.feature_profile.sdwan.transport.wan.vpn.routing.ospf
=======================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf
---------------------------------------------------------------------------------------------------------


Get WanVpn associated Routing Ospf Parcels for transport feature profile

.. code:: python

    def get_wan_vpn_associated_routing_ospf_parcels_for_transport(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospf.get_wan_vpn_associated_routing_ospf_parcels_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf
----------------------------------------------------------------------------------------------------------


Associate a wan/vpn parcel with a routing/ospf Parcel for transport feature profile

.. code:: python

    def create_wan_vpn_and_routing_ospf_parcel_association_for_transport(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospf.create_wan_vpn_and_routing_ospf_parcel_association_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf/{ospfId}
------------------------------------------------------------------------------------------------------------------


Get WanVpn parcel associated RoutingOspf Parcel by ospfId for transport feature profile

.. code:: python

    def get_wan_vpn_associated_routing_ospf_parcel_by_parcel_id_for_transport(
        transport_id: str, vpn_id: str, ospf_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospf.get_wan_vpn_associated_routing_ospf_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf/{ospfId}
------------------------------------------------------------------------------------------------------------------


Update a WanVpn parcel and a RoutingOspf Parcel association for transport feature profile

.. code:: python

    def edit_wan_vpn_and_routing_ospf_parcel_association_for_transport(
        transport_id: str,
        vpn_id: str,
        ospf_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospf.edit_wan_vpn_and_routing_ospf_parcel_association_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf/{ospfId}
---------------------------------------------------------------------------------------------------------------------


Delete a WanVpn parcel and a RoutingOspf Parcel association for transport feature profile

.. code:: python

    def delete_wan_vpn_and_routing_ospf_association_for_transport(
        transport_id: str, vpn_id: str, ospf_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospf.delete_wan_vpn_and_routing_ospf_association_for_transport()


