=============================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet
=============================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet
----------------------------------------------------------------------------------------------------------------


Create a WanVpn InterfaceEthernet parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_id: str,
        payload: CreateWanVpnInterfaceEthernetParcelForTransportPostRequest,
    ) -> CreateWanVpnInterfaceEthernetParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}
----------------------------------------------------------------------------------------------------------------------------


Update a WanVpn InterfaceEthernet Parcel for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        ethernet_id: str,
        payload: EditWanVpnInterfaceEthernetParcelForTransportPutRequest,
    ) -> EditWanVpnInterfaceEthernetParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}
-------------------------------------------------------------------------------------------------------------------------------


Delete a  WanVpn InterfaceEthernet Parcel for transport feature profile

.. code:: python

    def delete(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet
---------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str
    ) -> GetListSdwanTransportWanVpnInterfaceEthernetPayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}
----------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, ethernet_id: str
    ) -> GetSingleSdwanTransportWanVpnInterfaceEthernetPayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.get()


.. toctree::
    :maxdepth: 1

    schema/index
    ipv6_tracker/index
    ipv6_trackergroup/index
    tracker/index
    trackergroup/index
    models

