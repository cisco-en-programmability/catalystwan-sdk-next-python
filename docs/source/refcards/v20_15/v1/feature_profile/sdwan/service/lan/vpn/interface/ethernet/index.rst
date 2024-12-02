===========================================================
v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet
===========================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet
-----------------------------------------------------------------------------------------------------------


Get InterfaceEthernet Parcels for service LanVpn Parcel

.. code:: python

    def get_interface_ethernet_parcels_for_service_lan_vpn(
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.get_interface_ethernet_parcels_for_service_lan_vpn()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet
------------------------------------------------------------------------------------------------------------


Create a LanVpn InterfaceEthernet parcel for service feature profile

.. code:: python

    def create_lan_vpn_interface_ethernet_parcel_for_service(
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.create_lan_vpn_interface_ethernet_parcel_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}
------------------------------------------------------------------------------------------------------------------------


Get LanVpn InterfaceEthernet Parcel by ethernetId for service feature profile

.. code:: python

    def get_lan_vpn_interface_ethernet_parcel_by_parcel_id_for_service(
        service_id: str, vpn_id: str, ethernet_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.get_lan_vpn_interface_ethernet_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}
------------------------------------------------------------------------------------------------------------------------


Update a LanVpn InterfaceEthernet Parcel for service feature profile

.. code:: python

    def edit_lan_vpn_interface_ethernet_parcel_for_service(
        service_id: str,
        vpn_id: str,
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.edit_lan_vpn_interface_ethernet_parcel_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}
---------------------------------------------------------------------------------------------------------------------------


Delete a  LanVpn InterfaceEthernet Parcel for service feature profile

.. code:: python

    def delete_lan_vpn_interface_ethernet_for_service(
        service_id: str, vpn_id: str, ethernet_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.delete_lan_vpn_interface_ethernet_for_service()


.. toctree::
    :maxdepth: 1

    schema/index
    dhcp_server
    tracker
    trackergroup

