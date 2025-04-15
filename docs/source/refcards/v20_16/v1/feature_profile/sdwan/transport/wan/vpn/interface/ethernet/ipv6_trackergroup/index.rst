===============================================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.ipv6_trackergroup
===============================================================================


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/ipv6-trackergroup/{ipv6-trackergroupId}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------


Update a WanVpnInterfaceEthernet parcel and a IPv6 TrackerGroup Parcel association for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        ethernet_id: str,
        ipv6_trackergroup_id: str,
        payload: EditWanVpnInterfaceEthernetAndIpv6TrackerGroupParcelAssociationForTransportPutRequest,
    ) -> EditWanVpnInterfaceEthernetAndIpv6TrackerGroupParcelAssociationForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.ipv6_trackergroup.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/ipv6-trackergroup/{ipv6-trackergroupId}
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a WanVpnInterfaceEthernet and a IPv6 TrackerGroup Parcel association for transport feature profile

.. code:: python

    def delete(
        transport_id: str,
        vpn_id: str,
        ethernet_id: str,
        ipv6_trackergroup_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.ipv6_trackergroup.delete()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnParcelId}/interface/ethernet/{ethernetId}/ipv6-trackergroup
-----------------------------------------------------------------------------------------------------------------------------------------------------


Associate a WanVpnInterfaceEthernet parcel with a IPv6 TrackerGroup Parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_parcel_id: str,
        ethernet_id: str,
        payload: CreateWanVpnInterfaceEthernetAndIpv6TrackerGroupParcelAssociationForTransportPostRequest,
    ) -> CreateWanVpnInterfaceEthernetAndIpv6TrackerGroupParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.ipv6_trackergroup.post()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/ipv6-trackergroup
----------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, ethernet_id: str
    ) -> List[
        GetWanVpnInterfaceEthernetAssociatedIpv6TrackerGroupParcelsForTransportGetResponse
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.ipv6_trackergroup.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/ipv6-trackergroup/{ipv6-trackergroupId}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
        vpn_id: str,
        ethernet_id: str,
        ipv6_trackergroup_id: str,
    ) -> GetSingleSdwanTransportWanVpnInterfaceEthernetIpv6TrackergroupPayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.ipv6_trackergroup.get()


.. toctree::
    :maxdepth: 1

    models

