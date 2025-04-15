==========================================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.trackergroup
==========================================================================


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/trackergroup/{trackerGroupId}
----------------------------------------------------------------------------------------------------------------------------------------------------------


Update a WanVpnInterfaceCellular parcel and a Tracker Group Parcel association for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        cellular_id: str,
        tracker_group_id: str,
        payload: EditWanVpnInterfaceCellularAndTrackerGroupParcelAssociationForTransportPutRequest,
    ) -> EditWanVpnInterfaceCellularAndTrackerGroupParcelAssociationForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.trackergroup.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/trackergroup/{trackerGroupId}
-------------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a WanVpnInterfaceCellular and a Tracker Group Parcel association for transport feature profile

.. code:: python

    def delete(
        transport_id: str,
        vpn_id: str,
        cellular_id: str,
        tracker_group_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.trackergroup.delete()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnParcelId}/interface/cellular/{cellularId}/trackergroup
------------------------------------------------------------------------------------------------------------------------------------------------


Associate a WanVpnInterfaceCellular parcel with a TrackerGroup Parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_parcel_id: str,
        cellular_id: str,
        payload: CreateWanVpnInterfaceCellularAndTrackerGroupParcelAssociationForTransportPostRequest,
    ) -> CreateWanVpnInterfaceCellularAndTrackerGroupParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.trackergroup.post()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/trackergroup
-----------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, cellular_id: str
    ) -> List[
        GetWanVpnInterfaceCellularAssociatedTrackerGroupParcelsForTransportGetResponse
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.trackergroup.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/trackergroup/{trackerGroupId}
----------------------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
        vpn_id: str,
        cellular_id: str,
        tracker_group_id: str,
    ) -> (
        GetSingleSdwanTransportWanVpnInterfaceCellularTrackergroupPayload
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.trackergroup.get()


.. toctree::
    :maxdepth: 1

    models

