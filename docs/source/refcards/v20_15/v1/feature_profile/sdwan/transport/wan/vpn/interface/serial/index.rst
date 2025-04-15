===========================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.serial
===========================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/serial
--------------------------------------------------------------------------------------------------------------


Create a WanVpn InterfaceSerial parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_id: str,
        payload: CreateWanVpnInterfaceSerialParcelForTransportPostRequest,
    ) -> CreateWanVpnInterfaceSerialParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.serial.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/serial/{serialId}
------------------------------------------------------------------------------------------------------------------------


Update a WanVpn InterfaceSerial Parcel for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        serial_id: str,
        payload: EditWanVpnInterfaceSerialParcelForTransportPutRequest,
    ) -> EditWanVpnInterfaceSerialParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.serial.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/serial/{serialId}
---------------------------------------------------------------------------------------------------------------------------


Delete a  WanVpn InterfaceSerial Parcel for transport feature profile

.. code:: python

    def delete(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.serial.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/serial
-------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str
    ) -> GetListSdwanTransportWanVpnInterfaceSerialPayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.serial.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/serial/{serialId}
------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, serial_id: str
    ) -> GetSingleSdwanTransportWanVpnInterfaceSerialPayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.serial.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

