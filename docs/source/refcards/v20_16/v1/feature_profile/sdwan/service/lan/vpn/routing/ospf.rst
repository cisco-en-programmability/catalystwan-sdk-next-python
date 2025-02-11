=====================================================
v1.feature_profile.sdwan.service.lan.vpn.routing.ospf
=====================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospf
-----------------------------------------------------------------------------------------------------


Get LanVpn associated Routing Ospf Parcels for service feature profile

.. code:: python

    def get_lan_vpn_associated_routing_ospf_parcels_for_service(
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospf.get_lan_vpn_associated_routing_ospf_parcels_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospf
------------------------------------------------------------------------------------------------------


Associate a lanvpn parcel with a routingospf Parcel for service feature profile

.. code:: python

    def create_lan_vpn_and_routing_ospf_parcel_association_for_service(
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospf.create_lan_vpn_and_routing_ospf_parcel_association_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospf/{ospfId}
--------------------------------------------------------------------------------------------------------------


Get LanVpn parcel associated RoutingOspf Parcel by ospfId for service feature profile

.. code:: python

    def get_lan_vpn_associated_routing_ospf_parcel_by_parcel_id_for_service(
        service_id: str, vpn_id: str, ospf_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospf.get_lan_vpn_associated_routing_ospf_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospf/{ospfId}
--------------------------------------------------------------------------------------------------------------


Update a LanVpn parcel and a RoutingOspf Parcel association for service feature profile

.. code:: python

    def edit_lan_vpn_and_routing_ospf_parcel_association_for_service(
        service_id: str,
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospf.edit_lan_vpn_and_routing_ospf_parcel_association_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospf/{ospfId}
-----------------------------------------------------------------------------------------------------------------


Delete a LanVpn parcel and a RoutingOspf Parcel association for service feature profile

.. code:: python

    def delete_lan_vpn_and_routing_ospf_association_for_service(
        service_id: str, vpn_id: str, ospf_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospf.delete_lan_vpn_and_routing_ospf_association_for_service()


