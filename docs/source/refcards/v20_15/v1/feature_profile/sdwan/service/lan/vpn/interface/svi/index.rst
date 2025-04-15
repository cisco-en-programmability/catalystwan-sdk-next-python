======================================================
v1.feature_profile.sdwan.service.lan.vpn.interface.svi
======================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi
-------------------------------------------------------------------------------------------------------


Create a LanVpn InterfaceSvi parcel for service feature profile

.. code:: python

    def post(
        service_id: str,
        vpn_id: str,
        payload: CreateLanVpnInterfaceSviParcelForServicePostRequest,
    ) -> CreateLanVpnInterfaceSviParcelForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.svi.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}
--------------------------------------------------------------------------------------------------------------


Update a LanVpn InterfaceSvi Parcel for service feature profile

.. code:: python

    def put(
        service_id: str,
        vpn_id: str,
        svi_id: str,
        payload: EditLanVpnInterfaceSviParcelForServicePutRequest,
    ) -> EditLanVpnInterfaceSviParcelForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.svi.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}
-----------------------------------------------------------------------------------------------------------------


Delete a  LanVpn InterfaceSvi Parcel for service feature profile

.. code:: python

    def delete(service_id: str, vpn_id: str, svi_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.svi.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi
------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str
    ) -> GetListSdwanServiceLanVpnInterfaceSviPayload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.svi.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}
--------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str, svi_id: str
    ) -> GetSingleSdwanServiceLanVpnInterfaceSviPayload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.svi.get()


.. toctree::
    :maxdepth: 1

    schema/index
    dhcp_server/index
    models

