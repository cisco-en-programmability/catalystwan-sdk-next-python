==========================================================
v1.feature_profile.sdwan.service.lan.vpn.routing.multicast
==========================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast
----------------------------------------------------------------------------------------------------------


Get LanVpn associated Routing Multicast Parcels for service feature profile

.. code:: python

    def get_lan_vpn_associated_routing_multicast_parcels_for_service(
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.multicast.get_lan_vpn_associated_routing_multicast_parcels_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast
-----------------------------------------------------------------------------------------------------------


Associate a lanvpn parcel with a routingmulticast Parcel for service feature profile

.. code:: python

    def create_lan_vpn_and_routing_multicast_parcel_association_for_service(
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.multicast.create_lan_vpn_and_routing_multicast_parcel_association_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast/{multicastId}
------------------------------------------------------------------------------------------------------------------------


Get LanVpn parcel associated RoutingMulticast Parcel by multicastId for service feature profile

.. code:: python

    def get_lan_vpn_associated_routing_multicast_parcel_by_parcel_id_for_service(
        service_id: str, vpn_id: str, multicast_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.multicast.get_lan_vpn_associated_routing_multicast_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast/{multicastId}
------------------------------------------------------------------------------------------------------------------------


Update a LanVpn parcel and a RoutingMulticast Parcel association for service feature profile

.. code:: python

    def edit_lan_vpn_and_routing_multicast_parcel_association_for_service(
        service_id: str,
        vpn_id: str,
        multicast_id: str,
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.multicast.edit_lan_vpn_and_routing_multicast_parcel_association_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast/{multicastId}
---------------------------------------------------------------------------------------------------------------------------


Delete a LanVpn parcel and a RoutingMulticast Parcel association for service feature profile

.. code:: python

    def delete_lan_vpn_and_routing_multicast_association_for_service(
        service_id: str, vpn_id: str, multicast_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.multicast.delete_lan_vpn_and_routing_multicast_association_for_service()


