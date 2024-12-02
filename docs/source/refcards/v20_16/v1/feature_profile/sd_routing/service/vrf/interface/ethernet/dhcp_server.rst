========================================================================
v1.feature_profile.sd_routing.service.vrf.interface.ethernet.dhcp_server
========================================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server
-------------------------------------------------------------------------------------------------------------------------------------


Get the ethernet interface feature associated DHCP server feature in service feature profile

.. code:: python

    def get_vrf_interface_ethernet_associated_dhcp_server_parcels_for_service(
        service_id: str, vrf_id: str, ethernet_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.dhcp_server.get_vrf_interface_ethernet_associated_dhcp_server_parcels_for_service()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server
--------------------------------------------------------------------------------------------------------------------------------------


Associate a SD-Routing ethernet interface feature with a DHCP server feature for service feature profile

.. code:: python

    def create_vrf_interface_ethernet_and_dhcp_server_parcel_association_for_service(
        service_id: str,
        vrf_id: str,
        ethernet_id: str,
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.dhcp_server.create_vrf_interface_ethernet_and_dhcp_server_parcel_association_for_service()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server/{dhcpServerId}
----------------------------------------------------------------------------------------------------------------------------------------------------


Get the LAN ethernet interface feature associated DHCP server feature in service feature profile

.. code:: python

    def get_vrf_interface_ethernet_associated_dhcp_server_parcel_by_feature_id_for_service(
        service_id: str,
        vrf_id: str,
        ethernet_id: str,
        dhcp_server_id: str,
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.dhcp_server.get_vrf_interface_ethernet_associated_dhcp_server_parcel_by_feature_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server/{dhcpServerId}
----------------------------------------------------------------------------------------------------------------------------------------------------


Update a SD-Routing LAN ethernet interface feature and a DHCP server feature association for service feature profile

.. code:: python

    def edit_vrf_interface_ethernet_and_dhcp_server_parcel_association_for_service(
        service_id: str,
        vrf_id: str,
        ethernet_id: str,
        dhcp_server_id: str,
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.dhcp_server.edit_vrf_interface_ethernet_and_dhcp_server_parcel_association_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server/{dhcpServerId}
-------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a LAN ethernet interface feature and a DHCP server feature association for service feature profile

.. code:: python

    def delete_vrf_interface_ethernet_and_dhcp_server_association_for_service(
        service_id: str,
        vrf_id: str,
        ethernet_id: str,
        dhcp_server_id: str,
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.dhcp_server.delete_vrf_interface_ethernet_and_dhcp_server_association_for_service()


