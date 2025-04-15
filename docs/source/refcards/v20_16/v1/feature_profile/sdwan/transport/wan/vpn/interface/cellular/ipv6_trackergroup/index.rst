===============================================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_trackergroup
===============================================================================


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-trackergroup/{ipv6-trackergroupId}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------


Update a WanVpnInterfaceCellular parcel and a IPv6 TrackerGroup Parcel association for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        cellular_id: str,
        ipv6_trackergroup_id: str,
        payload: EditWanVpnInterfaceCellularAndIpv6TrackerGroupParcelAssociationForTransportPutRequest,
    ) -> EditWanVpnInterfaceCellularAndIpv6TrackerGroupParcelAssociationForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_trackergroup.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-trackergroup/{ipv6-trackergroupId}
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a WanVpnInterfaceCellular and a IPv6 TrackerGroup Parcel association for transport feature profile

.. code:: python

    def delete(
        transport_id: str,
        vpn_id: str,
        cellular_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_trackergroup.delete()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnParcelId}/interface/cellular/{cellularId}/ipv6-trackergroup
-----------------------------------------------------------------------------------------------------------------------------------------------------


Associate a WanVpnInterfaceCellular parcel with a IPv6 TrackerGroup Parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_parcel_id: str,
        cellular_id: str,
        payload: CreateWanVpnInterfaceCellularAndIpv6TrackerGroupParcelAssociationForTransportPostRequest,
    ) -> CreateWanVpnInterfaceCellularAndIpv6TrackerGroupParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_trackergroup.post()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-trackergroup
----------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, cellular_id: str
    ) -> List[
        GetWanVpnInterfaceCellularAssociatedIpv6TrackerGroupParcelsForTransportGetResponse
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_trackergroup.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-trackergroup/{ipv6-trackergroupId}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
        vpn_id: str,
        cellular_id: str,
        ipv6_trackergroup_id: str,
    ) -> GetSingleSdwanTransportWanVpnInterfaceCellularIpv6TrackergroupPayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_trackergroup.get()


.. toctree::
    :maxdepth: 1

    models

