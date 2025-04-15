========================================
v1.feature_profile.sdwan.service.lan.vpn
========================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn
---------------------------------------------------------------------------------


Create a Lan Vpn Profile Parcel for Service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateLanVpnProfileParcelForServicePostRequest,
    ) -> CreateLanVpnProfileParcelForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}
----------------------------------------------------------------------------------------


Update a Lan Vpn Profile Parcel for Service feature profile

.. code:: python

    def put(
        service_id: str,
        vpn_id: str,
        payload: EditLanVpnProfileParcelForServicePutRequest,
    ) -> EditLanVpnProfileParcelForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}
-------------------------------------------------------------------------------------------


Delete a Lan Vpn Profile Parcel for Service feature profile

.. code:: python

    def delete(service_id: str, vpn_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn
--------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(service_id: str) -> GetListSdwanServiceLanVpnPayload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}
----------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str
    ) -> GetSingleSdwanServiceLanVpnPayload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.get()


.. toctree::
    :maxdepth: 1

    interface/index
    schema/index
    routing/index
    models

