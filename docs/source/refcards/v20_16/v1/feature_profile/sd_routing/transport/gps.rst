===========================================
v1.feature_profile.sd_routing.transport.gps
===========================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/gps
-------------------------------------------------------------------------------------


Get GPS Profile Features for Transport feature profile

.. code:: python

    def get_gps_profile_parcel_for_transport(
        transport_id: str,
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
        client.v1.feature_profile.sd_routing.transport.gps.get_gps_profile_parcel_for_transport()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/gps
--------------------------------------------------------------------------------------


Create a GPS Profile Feature for Transport feature profile

.. code:: python

    def create_gps_profile_parcel_for_transport(
        transport_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.transport.gps.create_gps_profile_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/gps/{gpsId}
---------------------------------------------------------------------------------------------


Get GPS Profile Feature by parcelId for Transport feature profile

.. code:: python

    def get_gps_profile_parcel_by_parcel_id_for_transport(
        transport_id: str, gps_id: str
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
        client.v1.feature_profile.sd_routing.transport.gps.get_gps_profile_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/gps/{gpsId}
---------------------------------------------------------------------------------------------


Update a GPS Profile Feature for Transport feature profile

.. code:: python

    def edit_gps_profile_parcel_for_transport(
        transport_id: str, gps_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.transport.gps.edit_gps_profile_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/gps/{gpsId}
------------------------------------------------------------------------------------------------


Delete a GPS Profile Feature for Transport feature profile

.. code:: python

    def delete_gps_profile_parcel_for_transport(
        transport_id: str, gps_id: str
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
        client.v1.feature_profile.sd_routing.transport.gps.delete_gps_profile_parcel_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/{cellularControllerId}/gps/{gpsId}
--------------------------------------------------------------------------------------------------------------------


Update a CellularController feature and a GPS Parcel association for transport feature profile

.. code:: python

    def edit_cellular_controller_and_gps_parcel_association_for_transport_1(
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
        client.v1.feature_profile.sd_routing.transport.gps.edit_cellular_controller_and_gps_parcel_association_for_transport_1()


