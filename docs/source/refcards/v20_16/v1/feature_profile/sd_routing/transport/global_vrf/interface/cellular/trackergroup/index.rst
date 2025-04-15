==================================================================================
v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.trackergroup
==================================================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup
--------------------------------------------------------------------------------------------------------------------------------------------------


Associate a GlobalVRFInterfaceCellular feature with a Tracker Group Parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vrf_id: str,
        cellular_id: str,
        payload: CreateGlobalVrfInterfaceCellularAndTrackerParcelAssociationForTransportPostRequest,
    ) -> CreateGlobalVrfInterfaceCellularAndTrackerParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.trackergroup.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup/{trackerId}
-------------------------------------------------------------------------------------------------------------------------------------------------------------


Update a GlobalVRFInterfaceCellular feature and a Tracker Group Parcel association for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vrf_id: str,
        cellular_id: str,
        tracker_id: str,
        payload: EditGlobalVrfInterfaceCellularAndTrackerParcelAssociationForTransportPutRequest,
    ) -> EditGlobalVrfInterfaceCellularAndTrackerParcelAssociationForTransportPutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.trackergroup.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup/{trackerId}
----------------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a GlobalVRFInterfaceCellular and a Tracker Group Feature association for transport feature profile

.. code:: python

    def delete(
        transport_id: str, vrf_id: str, cellular_id: str, tracker_id: str
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.trackergroup.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup
-------------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str, cellular_id: str
    ) -> List[
        GetGlobalVrfInterfaceCellularAssociatedTrackerParcelsForTransportGetResponse
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.trackergroup.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup/{trackerId}
-------------------------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str, cellular_id: str, tracker_id: str
    ) -> GetSingleSdRoutingTransportGlobalVrfInterfaceCellularTrackergroupPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.trackergroup.get()


.. toctree::
    :maxdepth: 1

    models

