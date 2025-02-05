==================================================================================
v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.trackergroup
==================================================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup
-------------------------------------------------------------------------------------------------------------------------------------------------


Get GlobalVRFInterfaceCellular associated Tracker Group Features for transport feature profile

.. code:: python

    def get_global_vrf_interface_cellular_associated_tracker_parcels_for_transport(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.trackergroup.get_global_vrf_interface_cellular_associated_tracker_parcels_for_transport()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup
--------------------------------------------------------------------------------------------------------------------------------------------------


Associate a GlobalVRFInterfaceCellular feature with a Tracker Group Parcel for transport feature profile

.. code:: python

    def create_global_vrf_interface_cellular_and_tracker_parcel_association_for_transport(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.trackergroup.create_global_vrf_interface_cellular_and_tracker_parcel_association_for_transport()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup/{trackerId}
-------------------------------------------------------------------------------------------------------------------------------------------------------------


Get GlobalVRFInterfaceCellular associated Tracker Group Feature by trackerId for transport feature profile

.. code:: python

    def get_global_vrf_interface_cellular_associated_tracker_parcel_by_parcel_id_for_transport(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.trackergroup.get_global_vrf_interface_cellular_associated_tracker_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup/{trackerId}
-------------------------------------------------------------------------------------------------------------------------------------------------------------


Update a GlobalVRFInterfaceCellular feature and a Tracker Group Parcel association for transport feature profile

.. code:: python

    def edit_global_vrf_interface_cellular_and_tracker_parcel_association_for_transport(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.trackergroup.edit_global_vrf_interface_cellular_and_tracker_parcel_association_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{cellularId}/trackergroup/{trackerId}
----------------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a GlobalVRFInterfaceCellular and a Tracker Group Feature association for transport feature profile

.. code:: python

    def delete_global_vrf_interface_cellular_and_tracker_association_for_transport(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.trackergroup.delete_global_vrf_interface_cellular_and_tracker_association_for_transport()


