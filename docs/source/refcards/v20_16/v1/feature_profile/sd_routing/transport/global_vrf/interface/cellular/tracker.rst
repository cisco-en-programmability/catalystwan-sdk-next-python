=============================================================================
v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.tracker
=============================================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/tracker
--------------------------------------------------------------------------------------------------------------------------------------------


Get GlobalVRFInterfaceCellular associated Tracker Parcels for transport feature profile

.. code:: python

    def get_global_vrf_interface_cellular_associated_tracker_parcels_for_transport_1(
        transport_id: str, vrf_id: str, cellular_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.tracker.get_global_vrf_interface_cellular_associated_tracker_parcels_for_transport_1()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/tracker
---------------------------------------------------------------------------------------------------------------------------------------------


Associate a GlobalVRFInterfaceCellular parcel with a Tracker Parcel for transport feature profile

.. code:: python

    def create_global_vrf_interface_cellular_and_tracker_parcel_association_for_transport_1(
        transport_id: str,
        vrf_id: str,
        cellular_id: str,
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.tracker.create_global_vrf_interface_cellular_and_tracker_parcel_association_for_transport_1()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------------------------------------------------------------------


Get GlobalVRFInterfaceCellular associated Tracker Parcel by trackerId for transport feature profile

.. code:: python

    def get_global_vrf_interface_cellular_associated_tracker_parcel_by_parcel_id_for_transport_1(
        transport_id: str, vrf_id: str, cellular_id: str, tracker_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.tracker.get_global_vrf_interface_cellular_associated_tracker_parcel_by_parcel_id_for_transport_1()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------------------------------------------------------------------


Update a GlobalVRFInterfaceCellular parcel and a Tracker Parcel association for transport feature profile

.. code:: python

    def edit_global_vrf_interface_cellular_and_tracker_parcel_association_for_transport_1(
        transport_id: str,
        vrf_id: str,
        cellular_id: str,
        tracker_id: str,
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.tracker.edit_global_vrf_interface_cellular_and_tracker_parcel_association_for_transport_1()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/tracker/{trackerId}
-----------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a GlobalVRFInterfaceCellular and a Tracker Parcel association for transport feature profile

.. code:: python

    def delete_global_vrf_interface_cellular_and_tracker_association_for_transport_1(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.tracker.delete_global_vrf_interface_cellular_and_tracker_association_for_transport_1()


