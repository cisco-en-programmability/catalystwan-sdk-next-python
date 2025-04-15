==========================================
v1.feature_profile.sdwan.transport.wan.vpn
==========================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn
-------------------------------------------------------------------------------------


Create a Wan Vpn Profile Parcel for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateWanVpnProfileParcelForTransportPostRequest,
    ) -> CreateWanVpnProfileParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}
--------------------------------------------------------------------------------------------


Update a Wan Vpn Profile Parcel for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        payload: EditWanVpnProfileParcelForTransportPutRequest,
    ) -> EditWanVpnProfileParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}
-----------------------------------------------------------------------------------------------


Delete a Wan Vpn Profile Parcel for Transport feature profile

.. code:: python

    def delete(transport_id: str, vpn_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn
------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(transport_id: str) -> GetListSdwanTransportWanVpnPayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}
--------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str
    ) -> GetSingleSdwanTransportWanVpnPayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.get()


.. toctree::
    :maxdepth: 1

    interface/index
    schema/index
    routing/index
    models

