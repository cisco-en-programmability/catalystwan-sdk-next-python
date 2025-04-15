=============================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular
=============================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular
----------------------------------------------------------------------------------------------------------------


Create a wanvpn Cellular interface Parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_id: str,
        payload: CreateWanVpnInterfaceCellularParcelForTransportPostRequest,
    ) -> CreateWanVpnInterfaceCellularParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{intfId}
------------------------------------------------------------------------------------------------------------------------


Update a wanvpn Cellular Interface Parcel for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        intf_id: str,
        payload: EditWanVpnInterfaceCellularParcelForTransportPutRequest,
    ) -> EditWanVpnInterfaceCellularParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{intfId}
---------------------------------------------------------------------------------------------------------------------------


Delete a wanvpn Cellular interface Parcel for transport feature profile

.. code:: python

    def delete(transport_id: str, vpn_id: str, intf_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular
---------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str
    ) -> GetListSdwanTransportWanVpnInterfaceCellularPayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{intfId}
------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, intf_id: str
    ) -> GetSingleSdwanTransportWanVpnInterfaceCellularPayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.get()


.. toctree::
    :maxdepth: 1

    schema/index
    ipv6_tracker/index
    ipv6_trackergroup/index
    tracker/index
    trackergroup/index
    models

