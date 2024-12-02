=============================================
v1.feature_profile.sdwan.service.trackergroup
=============================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/trackergroup
-------------------------------------------------------------------------------------


Get TrackerGroup Profile Parcels for Service feature profile

.. code:: python

    def get_tracker_group_profile_parcel_for_service(
        service_id: str,
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
        client.v1.feature_profile.sdwan.service.trackergroup.get_tracker_group_profile_parcel_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/trackergroup
--------------------------------------------------------------------------------------


Create a TrackerGroup Profile Parcel for Service feature profile

.. code:: python

    def create_tracker_group_profile_parcel_for_service(
        service_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.service.trackergroup.create_tracker_group_profile_parcel_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/trackergroup/{trackergroupId}
------------------------------------------------------------------------------------------------------


Get TrackerGroup Profile Parcel by parcelId for Service feature profile

.. code:: python

    def get_tracker_group_profile_parcel_by_parcel_id_for_service(
        service_id: str, trackergroup_id: str
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
        client.v1.feature_profile.sdwan.service.trackergroup.get_tracker_group_profile_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/trackergroup/{trackergroupId}
------------------------------------------------------------------------------------------------------


Update a TrackerGroup Profile Parcel for Service feature profile

.. code:: python

    def edit_tracker_group_profile_parcel_for_service(
        service_id: str,
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
        client.v1.feature_profile.sdwan.service.trackergroup.edit_tracker_group_profile_parcel_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/trackergroup/{trackergroupId}
---------------------------------------------------------------------------------------------------------


Delete a TrackerGroup Profile Parcel for Service feature profile

.. code:: python

    def delete_tracker_group_profile_parcel_for_service(
        service_id: str, trackergroup_id: str
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
        client.v1.feature_profile.sdwan.service.trackergroup.delete_tracker_group_profile_parcel_for_service()


.. toctree::
    :maxdepth: 1

    schema/index

