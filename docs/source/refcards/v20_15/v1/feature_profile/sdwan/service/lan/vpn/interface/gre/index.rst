======================================================
v1.feature_profile.sdwan.service.lan.vpn.interface.gre
======================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/gre
-------------------------------------------------------------------------------------------------------


Create a LanVpn InterfaceGre for service feature profile

.. code:: python

    def post(
        service_id: str,
        vpn_id: str,
        payload: CreateLanVpnInterfaceGreForServicePostRequest,
    ) -> CreateLanVpnInterfaceGreForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.gre.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/gre/{greId}
--------------------------------------------------------------------------------------------------------------


Update a LanVpn InterfaceGre Feature for service feature profile

.. code:: python

    def put(
        service_id: str,
        vpn_id: str,
        gre_id: str,
        payload: EditLanVpnInterfaceGreForServicePutRequest,
    ) -> EditLanVpnInterfaceGreForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.gre.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/gre/{greId}
-----------------------------------------------------------------------------------------------------------------


Delete a  LanVpn InterfaceGre for service feature profile

.. code:: python

    def delete(service_id: str, vpn_id: str, gre_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.gre.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/gre
------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str
    ) -> GetListSdwanServiceLanVpnInterfaceGrePayload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.gre.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/gre/{greId}
--------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str, gre_id: str
    ) -> GetSingleSdwanServiceLanVpnInterfaceGrePayload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.gre.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

