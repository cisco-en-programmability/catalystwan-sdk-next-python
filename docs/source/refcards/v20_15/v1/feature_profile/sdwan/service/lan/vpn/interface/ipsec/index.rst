========================================================
v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec
========================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec
---------------------------------------------------------------------------------------------------------


Create a LanVpn InterfaceIpsec parcel for service feature profile

.. code:: python

    def post(
        service_id: str,
        vpn_id: str,
        payload: CreateIpSecProfileParcelPostRequest,
    ) -> CreateIpSecProfileParcelPostResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}
------------------------------------------------------------------------------------------------------------------


Update a LanVpn Interface Ipsec Parcel for Service feature profile

.. code:: python

    def put(
        service_id: str,
        vpn_id: str,
        ipsec_id: str,
        payload: EditProfileParcelPutRequest,
    ) -> EditProfileParcelPutResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}
---------------------------------------------------------------------------------------------------------------------


Delete a  LanVpn InterfaceIpsec Parcel for Service feature profile

.. code:: python

    def delete(service_id: str, vpn_id: str, ipsec_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec
--------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str
    ) -> GetListSdwanServiceLanVpnInterfaceIpsecPayload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}
------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str, ipsec_id: str
    ) -> GetSingleSdwanServiceLanVpnInterfaceIpsecPayload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.get()


.. toctree::
    :maxdepth: 1

    schema/index
    dhcp_server/index
    models

