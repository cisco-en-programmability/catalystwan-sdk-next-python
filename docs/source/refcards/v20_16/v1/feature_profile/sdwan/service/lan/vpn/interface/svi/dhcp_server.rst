==================================================================
v1.feature_profile.sdwan.service.lan.vpn.interface.svi.dhcp_server
==================================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}/dhcp-server
--------------------------------------------------------------------------------------------------------------------------


Get LanVpnInterfaceSvi associated DhcpServer Parcels for service feature profile

.. code:: python

    def get_lan_vpn_interface_svi_associated_dhcp_server_parcels_for_transport(
        service_id: str, vpn_id: str, svi_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.svi.dhcp_server.get_lan_vpn_interface_svi_associated_dhcp_server_parcels_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}/dhcp-server/{dhcpServerId}
-----------------------------------------------------------------------------------------------------------------------------------------


Get LanVpnInterfaceSvi associated DhcpServer Parcel by dhcpServerId for service feature profile

.. code:: python

    def get_lan_vpn_interface_svi_associated_dhcp_server_parcel_by_parcel_id_for_transport(
        service_id: str, vpn_id: str, svi_id: str, dhcp_server_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.svi.dhcp_server.get_lan_vpn_interface_svi_associated_dhcp_server_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}/dhcp-server/{dhcpServerId}
-----------------------------------------------------------------------------------------------------------------------------------------


Update a LanVpnInterfaceSvi parcel and a DhcpServer Parcel association for service feature profile

.. code:: python

    def edit_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport(
        service_id: str,
        vpn_id: str,
        svi_id: str,
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.svi.dhcp_server.edit_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}/dhcp-server/{dhcpServerId}
--------------------------------------------------------------------------------------------------------------------------------------------


Delete a LanVpnInterfaceSvi and a DhcpServer Parcel association for service feature profile

.. code:: python

    def delete_lan_vpn_interface_svi_and_dhcp_server_association_for_transport(
        service_id: str, vpn_id: str, svi_id: str, dhcp_server_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.svi.dhcp_server.delete_lan_vpn_interface_svi_and_dhcp_server_association_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnParcelId}/interface/svi/{sviId}/dhcp-server
---------------------------------------------------------------------------------------------------------------------------------


Associate a LanVpnInterfaceSvi parcel with a DhcpServer Parcel for service feature profile

.. code:: python

    def create_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport(
        service_id: str,
        vpn_parcel_id: str,
        svi_id: str,
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.svi.dhcp_server.create_lan_vpn_interface_svi_and_dhcp_server_parcel_association_for_transport()


