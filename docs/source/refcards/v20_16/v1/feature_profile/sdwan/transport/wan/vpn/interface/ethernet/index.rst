=============================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet
=============================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet
---------------------------------------------------------------------------------------------------------------


Get InterfaceEthernet Parcels for transport WanVpn Parcel

.. code:: python

    def get_interface_ethernet_parcels_for_transport_wan_vpn(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.get_interface_ethernet_parcels_for_transport_wan_vpn()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet
----------------------------------------------------------------------------------------------------------------


Create a WanVpn InterfaceEthernet parcel for transport feature profile

.. code:: python

    def create_wan_vpn_interface_ethernet_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.create_wan_vpn_interface_ethernet_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}
----------------------------------------------------------------------------------------------------------------------------


Get WanVpn InterfaceEthernet Parcel by ethernetId for transport feature profile

.. code:: python

    def get_wan_vpn_interface_ethernet_parcel_by_parcel_id_for_transport(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.get_wan_vpn_interface_ethernet_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}
----------------------------------------------------------------------------------------------------------------------------


Update a WanVpn InterfaceEthernet Parcel for transport feature profile

.. code:: python

    def edit_wan_vpn_interface_ethernet_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.edit_wan_vpn_interface_ethernet_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}
-------------------------------------------------------------------------------------------------------------------------------


Delete a  WanVpn InterfaceEthernet Parcel for transport feature profile

.. code:: python

    def delete_wan_vpn_interface_ethernet_for_transport(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.delete_wan_vpn_interface_ethernet_for_transport()


.. toctree::
    :maxdepth: 1

    schema/index
    ipv6_tracker
    ipv6_trackergroup
    tracker
    trackergroup

