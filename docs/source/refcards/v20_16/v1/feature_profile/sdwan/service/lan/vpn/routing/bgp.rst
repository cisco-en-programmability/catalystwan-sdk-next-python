====================================================
v1.feature_profile.sdwan.service.lan.vpn.routing.bgp
====================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp
----------------------------------------------------------------------------------------------------


Get LanVpn associated Routing Bgp Parcels for service feature profile

.. code:: python

    def get_lan_vpn_associated_routing_bgp_parcels_for_service(
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.bgp.get_lan_vpn_associated_routing_bgp_parcels_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp
-----------------------------------------------------------------------------------------------------


Associate a lanvpn parcel with a routingbgp Parcel for service feature profile

.. code:: python

    def create_lan_vpn_and_routing_bgp_parcel_association_for_service(
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.bgp.create_lan_vpn_and_routing_bgp_parcel_association_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp/{bgpId}
------------------------------------------------------------------------------------------------------------


Get LanVpn parcel associated RoutingBgp Parcel by bgpId for service feature profile

.. code:: python

    def get_lan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_service(
        service_id: str, vpn_id: str, bgp_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.bgp.get_lan_vpn_associated_routing_bgp_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp/{bgpId}
------------------------------------------------------------------------------------------------------------


Update a LanVpn parcel and a RoutingBgp Parcel association for service feature profile

.. code:: python

    def edit_lan_vpn_and_routing_bgp_parcel_association_for_service(
        service_id: str,
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.bgp.edit_lan_vpn_and_routing_bgp_parcel_association_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp/{bgpId}
---------------------------------------------------------------------------------------------------------------


Delete a LanVpn parcel and a RoutingBgp Parcel association for service feature profile

.. code:: python

    def delete_lan_vpn_and_routing_bgp_association_for_service(
        service_id: str, vpn_id: str, bgp_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.bgp.delete_lan_vpn_and_routing_bgp_association_for_service()


