====================================================================
v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.dhcp_server
====================================================================


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}/dhcp-server/{dhcpServerId}
---------------------------------------------------------------------------------------------------------------------------------------------


Update a LanVpnInterfaceIpsec parcel and a DhcpServer Parcel association for service feature profile

.. code:: python

    def put(
        service_id: str,
        vpn_id: str,
        ipsec_id: str,
        dhcp_server_id: str,
        payload: EditLanVpnInterfaceIpsecAndDhcpServerParcelAssociationForTransportPutRequest,
    ) -> EditLanVpnInterfaceIpsecAndDhcpServerParcelAssociationForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.dhcp_server.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}/dhcp-server/{dhcpServerId}
------------------------------------------------------------------------------------------------------------------------------------------------


Delete a LanVpnInterfaceIpsec and a DhcpServer Parcel association for service feature profile

.. code:: python

    def delete(
        service_id: str, vpn_id: str, ipsec_id: str, dhcp_server_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.dhcp_server.delete()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnParcelId}/interface/ipsec/{ipsecId}/dhcp-server
-------------------------------------------------------------------------------------------------------------------------------------


Associate a LanVpnInterfaceIpsec parcel with a DhcpServer Parcel for service feature profile

.. code:: python

    def post(
        service_id: str,
        vpn_parcel_id: str,
        ipsec_id: str,
        payload: CreateLanVpnInterfaceIpsecAndDhcpServerParcelAssociationForTransportPostRequest,
    ) -> CreateLanVpnInterfaceIpsecAndDhcpServerParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.dhcp_server.post()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}/dhcp-server
------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str, ipsec_id: str
    ) -> List[
        GetLanVpnInterfaceIpsecAssociatedDhcpServerParcelsForTransportGetResponse
    ]: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.dhcp_server.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}/dhcp-server/{dhcpServerId}
---------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str, ipsec_id: str, dhcp_server_id: str
    ) -> GetSingleSdwanServiceLanVpnInterfaceIpsecDhcpServerPayload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.dhcp_server.get()


.. toctree::
    :maxdepth: 1

    models

