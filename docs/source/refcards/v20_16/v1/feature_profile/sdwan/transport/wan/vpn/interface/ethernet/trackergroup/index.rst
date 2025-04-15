==========================================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.trackergroup
==========================================================================


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup/{trackergroupId}
----------------------------------------------------------------------------------------------------------------------------------------------------------


Update a WanVpnInterfaceEthernet parcel and a TrackerGroup Parcel association for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        ethernet_id: str,
        trackergroup_id: str,
        payload: EditWanVpnInterfaceEthernetAndTrackerGroupParcelAssociationForTransportPutRequest,
    ) -> EditWanVpnInterfaceEthernetAndTrackerGroupParcelAssociationForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.trackergroup.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup/{trackergroupId}
-------------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a WanVpnInterfaceEthernet and a TrackerGroup Parcel association for transport feature profile

.. code:: python

    def delete(
        transport_id: str,
        vpn_id: str,
        ethernet_id: str,
        trackergroup_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.trackergroup.delete()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnParcelId}/interface/ethernet/{ethernetId}/trackergroup
------------------------------------------------------------------------------------------------------------------------------------------------


Associate a WanVpnInterfaceEthernet parcel with a TrackerGroup Parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_parcel_id: str,
        ethernet_id: str,
        payload: CreateWanVpnInterfaceEthernetAndTrackerGroupParcelAssociationForTransportPostRequest,
    ) -> CreateWanVpnInterfaceEthernetAndTrackerGroupParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.trackergroup.post()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup
-----------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, ethernet_id: str
    ) -> List[
        GetWanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransportGetResponse
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.trackergroup.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup/{trackergroupId}
----------------------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
        vpn_id: str,
        ethernet_id: str,
        trackergroup_id: str,
    ) -> (
        GetSingleSdwanTransportWanVpnInterfaceEthernetTrackergroupPayload
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.trackergroup.get()


.. toctree::
    :maxdepth: 1

    models

