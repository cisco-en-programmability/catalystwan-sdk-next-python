==========================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec
==========================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec
-------------------------------------------------------------------------------------------------------------


Create a WanVpn InterfaceIpsec parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_id: str,
        payload: CreateIpSecProfileParcel1PostRequest,
    ) -> CreateIpSecProfileParcel1PostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec/{ipsecId}
----------------------------------------------------------------------------------------------------------------------


Update a WanVpn InterfaceIpsec Parcel for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        ipsec_id: str,
        payload: EditProfileParcel1PutRequest,
    ) -> EditProfileParcel1PutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec/{ipsecId}
-------------------------------------------------------------------------------------------------------------------------


Delete a  WanVpn InterfaceIpsec Parcel for transport feature profile

.. code:: python

    def delete(transport_id: str, vpn_id: str, ipsec_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec
------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str
    ) -> GetListSdwanTransportWanVpnInterfaceIpsecPayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec/{ipsecId}
----------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, ipsec_id: str
    ) -> GetSingleSdwanTransportWanVpnInterfaceIpsecPayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.get()


.. toctree::
    :maxdepth: 1

    schema/index
    tracker/index
    models

