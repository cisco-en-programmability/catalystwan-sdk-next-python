====================================================================
v1.feature_profile.sdwan.transport.management.vpn.interface.ethernet
====================================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}/interface/ethernet
-----------------------------------------------------------------------------------------------------------------------


Create a ManagementVpn InterfaceEthernet parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_id: str,
        payload: CreateManagementVpnInterfaceEthernetParcelForTransportPostRequest,
    ) -> (
        CreateManagementVpnInterfaceEthernetParcelForTransportPostResponse
    ): ...


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
        client.v1.feature_profile.sdwan.transport.management.vpn.interface.ethernet.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}/interface/ethernet/{ethernetId}
-----------------------------------------------------------------------------------------------------------------------------------


Update a ManagementVpn InterfaceEthernet Parcel for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        ethernet_id: str,
        payload: EditManagementVpnInterfaceEthernetParcelForTransportPutRequest,
    ) -> (
        EditManagementVpnInterfaceEthernetParcelForTransportPutResponse
    ): ...


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
        client.v1.feature_profile.sdwan.transport.management.vpn.interface.ethernet.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}/interface/ethernet/{ethernetId}
--------------------------------------------------------------------------------------------------------------------------------------


Delete a  ManagementVpn InterfaceEthernet Parcel for transport feature profile

.. code:: python

    def delete(
        transport_id: str, vpn_id: str, ethernet_id: str
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
        client.v1.feature_profile.sdwan.transport.management.vpn.interface.ethernet.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}/interface/ethernet
----------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str
    ) -> GetListSdwanTransportManagementVpnInterfaceEthernetPayload: ...


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
        client.v1.feature_profile.sdwan.transport.management.vpn.interface.ethernet.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}/interface/ethernet/{ethernetId}
-----------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, ethernet_id: str
    ) -> GetSingleSdwanTransportManagementVpnInterfaceEthernetPayload: ...


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
        client.v1.feature_profile.sdwan.transport.management.vpn.interface.ethernet.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

