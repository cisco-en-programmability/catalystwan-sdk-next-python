=================================================
v1.feature_profile.sdwan.transport.management.vpn
=================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn
--------------------------------------------------------------------------------------------


Create a Management Vpn Profile Parcel for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateManagementVpnProfileParcelForTransportPostRequest,
    ) -> CreateManagementVpnProfileParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.management.vpn.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}
---------------------------------------------------------------------------------------------------


Update a Management Vpn Profile Parcel for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        payload: EditManagementVpnProfileParcelForTransportPutRequest,
    ) -> EditManagementVpnProfileParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.management.vpn.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}
------------------------------------------------------------------------------------------------------


Delete a Management Vpn Profile Parcel for Transport feature profile

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
        client.v1.feature_profile.sdwan.transport.management.vpn.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn
-------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdwanTransportManagementVpnPayload: ...


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
        client.v1.feature_profile.sdwan.transport.management.vpn.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}
---------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str
    ) -> GetSingleSdwanTransportManagementVpnPayload: ...


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
        client.v1.feature_profile.sdwan.transport.management.vpn.get()


.. toctree::
    :maxdepth: 1

    interface/index
    schema/index
    models

