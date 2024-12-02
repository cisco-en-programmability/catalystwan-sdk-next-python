===========================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.serial
===========================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/serial
-------------------------------------------------------------------------------------------------------------


Get InterfaceSerial Parcels for transport WanVpn Parcel

.. code:: python

    def get_interface_serial_parcels_for_transport_wan_vpn(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.serial.get_interface_serial_parcels_for_transport_wan_vpn()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/serial
--------------------------------------------------------------------------------------------------------------


Create a WanVpn InterfaceSerial parcel for transport feature profile

.. code:: python

    def create_wan_vpn_interface_serial_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.serial.create_wan_vpn_interface_serial_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/serial/{serialId}
------------------------------------------------------------------------------------------------------------------------


Get WanVpn InterfaceSerial Parcel by serialId for transport feature profile

.. code:: python

    def get_wan_vpn_interface_serial_parcel_by_parcel_id_for_transport(
        transport_id: str, vpn_id: str, serial_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.serial.get_wan_vpn_interface_serial_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/serial/{serialId}
------------------------------------------------------------------------------------------------------------------------


Update a WanVpn InterfaceSerial Parcel for transport feature profile

.. code:: python

    def edit_wan_vpn_interface_serial_parcel_for_transport(
        transport_id: str,
        vpn_id: str,
        serial_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.serial.edit_wan_vpn_interface_serial_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/serial/{serialId}
---------------------------------------------------------------------------------------------------------------------------


Delete a  WanVpn InterfaceSerial Parcel for transport feature profile

.. code:: python

    def delete_wan_vpn_interface_serial_for_transport(
        transport_id: str, vpn_id: str, serial_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.serial.delete_wan_vpn_interface_serial_for_transport()


.. toctree::
    :maxdepth: 1

    schema/index

