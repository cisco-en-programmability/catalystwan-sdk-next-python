==========================================================
v1.feature_profile.sdwan.transport.cellular_controller.gps
==========================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps
---------------------------------------------------------------------------------------------------------------------------


Get CellularController associated Gps Parcels for transport feature profile

.. code:: python

    def get_cellular_controller_associated_gps_parcels_for_transport(
        transport_id: str, cellular_controller_id: str
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
        client.v1.feature_profile.sdwan.transport.cellular_controller.gps.get_cellular_controller_associated_gps_parcels_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps
----------------------------------------------------------------------------------------------------------------------------


Associate a cellularcontroller parcel with a gps Parcel for transport feature profile

.. code:: python

    def create_cellular_controller_and_gps_parcel_association_for_transport(
        transport_id: str,
        cellular_controller_id: str,
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
        client.v1.feature_profile.sdwan.transport.cellular_controller.gps.create_cellular_controller_and_gps_parcel_association_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps/{gpsId}
-----------------------------------------------------------------------------------------------------------------------------------


Get CellularController parcel associated Gps Parcel by gpsId for transport feature profile

.. code:: python

    def get_cellular_controller_associated_gps_parcel_by_parcel_id_for_transport(
        transport_id: str, cellular_controller_id: str, gps_id: str
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
        client.v1.feature_profile.sdwan.transport.cellular_controller.gps.get_cellular_controller_associated_gps_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps/{gpsId}
-----------------------------------------------------------------------------------------------------------------------------------


Update a CellularController parcel and a Gps Parcel association for transport feature profile

.. code:: python

    def edit_cellular_controller_and_gps_parcel_association_for_transport(
        transport_id: str,
        cellular_controller_id: str,
        gps_id: str,
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
        client.v1.feature_profile.sdwan.transport.cellular_controller.gps.edit_cellular_controller_and_gps_parcel_association_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps/{gpsId}
--------------------------------------------------------------------------------------------------------------------------------------


Delete a CellularController parcel and a Gps Parcel association for transport feature profile

.. code:: python

    def delete_cellular_controller_and_gps_association_for_transport(
        transport_id: str, cellular_controller_id: str, gps_id: str
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
        client.v1.feature_profile.sdwan.transport.cellular_controller.gps.delete_cellular_controller_and_gps_association_for_transport()


