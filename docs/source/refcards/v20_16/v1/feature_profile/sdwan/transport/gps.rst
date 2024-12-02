======================================
v1.feature_profile.sdwan.transport.gps
======================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/gps
--------------------------------------------------------------------------------


Get Gps Profile Parcels for Transport feature profile

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
        client.v1.feature_profile.sdwan.transport.gps.get_gps_profile_parcel_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/gps
---------------------------------------------------------------------------------


Create a Gps Profile Parcel for Transport feature profile

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
        client.v1.feature_profile.sdwan.transport.gps.create_gps_profile_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/gps/{gpsId}
----------------------------------------------------------------------------------------


Get Gps Profile Parcel by parcelId for Transport feature profile

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
        client.v1.feature_profile.sdwan.transport.gps.get_gps_profile_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/gps/{gpsId}
----------------------------------------------------------------------------------------


Update a Gps Profile Parcel for Transport feature profile

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
        client.v1.feature_profile.sdwan.transport.gps.edit_gps_profile_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/gps/{gpsId}
-------------------------------------------------------------------------------------------


Delete a Gps Profile Parcel for Transport feature profile

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
        client.v1.feature_profile.sdwan.transport.gps.delete_gps_profile_parcel_for_transport()


