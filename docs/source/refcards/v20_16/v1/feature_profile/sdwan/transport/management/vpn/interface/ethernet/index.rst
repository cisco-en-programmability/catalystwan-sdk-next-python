====================================================================
v1.feature_profile.sdwan.transport.management.vpn.interface.ethernet
====================================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}/interface/ethernet
----------------------------------------------------------------------------------------------------------------------


Get InterfaceEthernet Parcels for transport ManagementVpn Parcel

.. code:: python

    def get_interface_ethernet_parcels_for_transport_management_vpn(
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
        client.v1.feature_profile.sdwan.transport.management.vpn.interface.ethernet.get_interface_ethernet_parcels_for_transport_management_vpn()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}/interface/ethernet
-----------------------------------------------------------------------------------------------------------------------


Create a ManagementVpn InterfaceEthernet parcel for transport feature profile

.. code:: python

    def create_management_vpn_interface_ethernet_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.management.vpn.interface.ethernet.create_management_vpn_interface_ethernet_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}/interface/ethernet/{ethernetId}
-----------------------------------------------------------------------------------------------------------------------------------


Get ManagementVpn InterfaceEthernet Parcel by ethernetId for transport feature profile

.. code:: python

    def get_management_vpn_interface_ethernet_parcel_by_parcel_id_for_transport(
        transport_id: str, vpn_id: str, ethernet_id: str
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
        client.v1.feature_profile.sdwan.transport.management.vpn.interface.ethernet.get_management_vpn_interface_ethernet_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}/interface/ethernet/{ethernetId}
-----------------------------------------------------------------------------------------------------------------------------------


Update a ManagementVpn InterfaceEthernet Parcel for transport feature profile

.. code:: python

    def edit_management_vpn_interface_ethernet_parcel_for_transport(
        transport_id: str,
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
        client.v1.feature_profile.sdwan.transport.management.vpn.interface.ethernet.edit_management_vpn_interface_ethernet_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}/interface/ethernet/{ethernetId}
--------------------------------------------------------------------------------------------------------------------------------------


Delete a  ManagementVpn InterfaceEthernet Parcel for transport feature profile

.. code:: python

    def delete_management_vpn_interface_ethernet_for_transport(
        transport_id: str, vpn_id: str, ethernet_id: str
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
        client.v1.feature_profile.sdwan.transport.management.vpn.interface.ethernet.delete_management_vpn_interface_ethernet_for_transport()


.. toctree::
    :maxdepth: 1

    schema/index

