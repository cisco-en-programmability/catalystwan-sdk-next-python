======================================================
v1.feature_profile.sdwan.service.lan.vpn.routing.eigrp
======================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp
------------------------------------------------------------------------------------------------------


Get LanVpn associated Routing Eigrp Features for service feature profile

.. code:: python

    def get_lan_vpn_associated_routing_eigrp_parcels_for_service(
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.eigrp.get_lan_vpn_associated_routing_eigrp_parcels_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp
-------------------------------------------------------------------------------------------------------


Associate a lanvpn feature with a routingeigrp Feature for service feature profile

.. code:: python

    def create_lan_vpn_and_routing_eigrp_parcel_association_for_service(
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.eigrp.create_lan_vpn_and_routing_eigrp_parcel_association_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp/{eigrpId}
----------------------------------------------------------------------------------------------------------------


Get LanVpn feature associated RoutingEigrp Feature by eigrpId for service feature profile

.. code:: python

    def get_lan_vpn_associated_routing_eigrp_parcel_by_parcel_id_for_service(
        service_id: str, vpn_id: str, eigrp_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.eigrp.get_lan_vpn_associated_routing_eigrp_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp/{eigrpId}
----------------------------------------------------------------------------------------------------------------


Update a LanVpn feature and a RoutingEigrp Feature association for service feature profile

.. code:: python

    def edit_lan_vpn_and_routing_eigrp_parcel_association_for_service(
        service_id: str,
        vpn_id: str,
        eigrp_id: str,
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.eigrp.edit_lan_vpn_and_routing_eigrp_parcel_association_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp/{eigrpId}
-------------------------------------------------------------------------------------------------------------------


Delete a LanVpn feature and a RoutingEigrp Feature association for service feature profile

.. code:: python

    def delete_lan_vpn_and_routing_eigrp_association_for_service(
        service_id: str, vpn_id: str, eigrp_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.eigrp.delete_lan_vpn_and_routing_eigrp_association_for_service()


