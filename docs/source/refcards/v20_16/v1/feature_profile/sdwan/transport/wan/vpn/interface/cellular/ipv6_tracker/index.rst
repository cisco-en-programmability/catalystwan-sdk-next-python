==========================================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_tracker
==========================================================================


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-tracker/{ipv6-trackerId}
----------------------------------------------------------------------------------------------------------------------------------------------------------


Update a WanVpnInterfaceCellular parcel and a IPv6 Tracker Parcel association for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        cellular_id: str,
        ipv6_tracker_id: str,
        payload: EditWanVpnInterfaceCellularAndIpv6TrackerParcelAssociationForTransportPutRequest,
    ) -> EditWanVpnInterfaceCellularAndIpv6TrackerParcelAssociationForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_tracker.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-tracker/{ipv6-trackerId}
-------------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a WanVpnInterfaceCellular and a IPv6 Tracker Parcel association for transport feature profile

.. code:: python

    def delete(
        transport_id: str,
        vpn_id: str,
        cellular_id: str,
        ipv6_tracker_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_tracker.delete()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnParcelId}/interface/cellular/{cellularId}/ipv6-tracker
------------------------------------------------------------------------------------------------------------------------------------------------


Associate a WanVpnInterfaceCellular parcel with a IPv6 Tracker Parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_parcel_id: str,
        cellular_id: str,
        payload: CreateWanVpnInterfaceCellularAndIpv6TrackerParcelAssociationForTransportPostRequest,
    ) -> CreateWanVpnInterfaceCellularAndIpv6TrackerParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_tracker.post()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-tracker
-----------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, cellular_id: str
    ) -> List[
        GetWanVpnInterfaceCellularAssociatedIpv6TrackerParcelsForTransportGetResponse
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_tracker.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-tracker/{ipv6-trackerId}
----------------------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
        vpn_id: str,
        cellular_id: str,
        ipv6_tracker_id: str,
    ) -> (
        GetSingleSdwanTransportWanVpnInterfaceCellularIpv6TrackerPayload
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_tracker.get()


.. toctree::
    :maxdepth: 1

    models

