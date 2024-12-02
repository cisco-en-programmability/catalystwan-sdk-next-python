============================================================
v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv6
============================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6
------------------------------------------------------------------------------------------------------------


Get LanVpn associated IPv6 address family OSPFv3 Parcels for service feature profile

.. code:: python

    def get_lan_vpn_associated_routing_ospfv3_i_pv6_parcels_for_service(
        service_id: str, vpn_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv6.get_lan_vpn_associated_routing_ospfv3_i_pv6_parcels_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6
-------------------------------------------------------------------------------------------------------------


Associate a LAN VPN parcel with a IPv6 address family OSPFv3 Parcel for service feature profile

.. code:: python

    def create_lan_vpn_and_routing_ospfv3_i_pv6_parcel_association_for_service(
        service_id: str, vpn_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv6.create_lan_vpn_and_routing_ospfv3_i_pv6_parcel_association_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6/{ospfv3Id}
-----------------------------------------------------------------------------------------------------------------------


Get LanVpn parcel associated IPv6 address family OSPFv3 IPv6 Parcel by ospfv3Id for service feature profile

.. code:: python

    def get_lan_vpn_associated_routing_ospfv3_i_pv6_parcel_by_parcel_id_for_service(
        service_id: str, vpn_id: str, ospfv3_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv6.get_lan_vpn_associated_routing_ospfv3_i_pv6_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6/{ospfv3Id}
-----------------------------------------------------------------------------------------------------------------------


Update a LAN VPN parcel and a routing OSPFv3 IPv6 Parcel association for service feature profile

.. code:: python

    def edit_lan_vpn_and_routing_ospfv3_i_pv6_parcel_association_for_service(
        service_id: str,
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv6.edit_lan_vpn_and_routing_ospfv3_i_pv6_parcel_association_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6/{ospfv3Id}
--------------------------------------------------------------------------------------------------------------------------


Delete a LAN VPN parcel and a IPv6 OSPFv3 parcel association for service feature profile

.. code:: python

    def delete_lan_vpn_and_routing_ospfv3_association_for_service_1(
        service_id: str, vpn_id: str, ospfv3_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv6.delete_lan_vpn_and_routing_ospfv3_association_for_service_1()


