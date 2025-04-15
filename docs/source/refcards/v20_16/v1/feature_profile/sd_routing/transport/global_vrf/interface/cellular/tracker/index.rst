=============================================================================
v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.tracker
=============================================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/tracker
---------------------------------------------------------------------------------------------------------------------------------------------


Associate a GlobalVRFInterfaceCellular parcel with a Tracker Parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vrf_id: str,
        cellular_id: str,
        payload: CreateGlobalVrfInterfaceCellularAndTrackerParcelAssociationForTransport1PostRequest,
    ) -> CreateGlobalVrfInterfaceCellularAndTrackerParcelAssociationForTransport1PostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.tracker.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------------------------------------------------------------------


Update a GlobalVRFInterfaceCellular parcel and a Tracker Parcel association for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vrf_id: str,
        cellular_id: str,
        tracker_id: str,
        payload: EditGlobalVrfInterfaceCellularAndTrackerParcelAssociationForTransport1PutRequest,
    ) -> EditGlobalVrfInterfaceCellularAndTrackerParcelAssociationForTransport1PutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.tracker.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/tracker/{trackerId}
-----------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a GlobalVRFInterfaceCellular and a Tracker Parcel association for transport feature profile

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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.tracker.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/tracker
--------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str, cellular_id: str
    ) -> List[
        GetGlobalVrfInterfaceCellularAssociatedTrackerParcelsForTransport1GetResponse
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.tracker.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str, cellular_id: str, tracker_id: str
    ) -> GetSingleSdRoutingTransportGlobalVrfInterfaceCellularTrackerPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.tracker.get()


.. toctree::
    :maxdepth: 1

    models

