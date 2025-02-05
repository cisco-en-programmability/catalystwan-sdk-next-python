===============================================
v1.feature_profile.sdwan.transport.trackergroup
===============================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/trackergroup
-----------------------------------------------------------------------------------------


Get TrackerGroup Profile Parcels for Transport feature profile

.. code:: python

    def get_tracker_group_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.trackergroup.get_tracker_group_profile_parcel_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/trackergroup
------------------------------------------------------------------------------------------


Create a TrackerGroup Profile Parcel for Transport feature profile

.. code:: python

    def create_tracker_group_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.trackergroup.create_tracker_group_profile_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/trackergroup/{trackergroupId}
----------------------------------------------------------------------------------------------------------


Get TrackerGroup Profile Parcel by parcelId for Transport feature profile

.. code:: python

    def get_tracker_group_profile_parcel_by_parcel_id_for_transport(
        transport_id: str, trackergroup_id: str
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
        client.v1.feature_profile.sdwan.transport.trackergroup.get_tracker_group_profile_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/trackergroup/{trackergroupId}
----------------------------------------------------------------------------------------------------------


Update a TrackerGroup Profile Parcel for Transport feature profile

.. code:: python

    def edit_tracker_group_profile_parcel_for_transport(
        transport_id: str,
        trackergroup_id: str,
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
        client.v1.feature_profile.sdwan.transport.trackergroup.edit_tracker_group_profile_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/trackergroup/{trackergroupId}
-------------------------------------------------------------------------------------------------------------


Delete a TrackerGroup Profile Parcel for Transport feature profile

.. code:: python

    def delete_tracker_group_profile_parcel_for_transport(
        transport_id: str, trackergroup_id: str
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
        client.v1.feature_profile.sdwan.transport.trackergroup.delete_tracker_group_profile_parcel_for_transport()


.. toctree::
    :maxdepth: 1

    schema/index

