========================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.gre
========================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre
-----------------------------------------------------------------------------------------------------------


Create a WanVpn InterfaceGre parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_id: str,
        payload: CreateWanVpnInterfaceGreParcelForTransportPostRequest,
    ) -> CreateWanVpnInterfaceGreParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}
------------------------------------------------------------------------------------------------------------------


Update a WanVpn InterfaceGre Parcel for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        gre_id: str,
        payload: EditWanVpnInterfaceGreParcelForTransportPutRequest,
    ) -> EditWanVpnInterfaceGreParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}
---------------------------------------------------------------------------------------------------------------------


Delete a  WanVpn InterfaceGre Parcel for transport feature profile

.. code:: python

    def delete(transport_id: str, vpn_id: str, gre_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre
----------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str
    ) -> GetListSdwanTransportWanVpnInterfaceGrePayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}
------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, gre_id: str
    ) -> GetSingleSdwanTransportWanVpnInterfaceGrePayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.get()


.. toctree::
    :maxdepth: 1

    schema/index
    tracker/index
    models

