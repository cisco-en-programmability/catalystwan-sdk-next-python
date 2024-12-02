========================================
v1.feature_profile.sdwan.service.tracker
========================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/tracker
--------------------------------------------------------------------------------


Get Tracker Profile Parcels for Service feature profile

.. code:: python

    def get_tracker_profile_parcel_for_service(
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
        client.v1.feature_profile.sdwan.service.tracker.get_tracker_profile_parcel_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/tracker
---------------------------------------------------------------------------------


Create a Tracker Profile Parcel for Service feature profile

.. code:: python

    def create_tracker_profile_parcel_for_service(
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
        client.v1.feature_profile.sdwan.service.tracker.create_tracker_profile_parcel_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------


Get Tracker Profile Parcel by parcelId for Service feature profile

.. code:: python

    def get_tracker_profile_parcel_by_parcel_id_for_service(
        service_id: str, tracker_id: str
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
        client.v1.feature_profile.sdwan.service.tracker.get_tracker_profile_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------


Update a Tracker Profile Parcel for Service feature profile

.. code:: python

    def edit_tracker_profile_parcel_for_service(
        service_id: str, tracker_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.service.tracker.edit_tracker_profile_parcel_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/tracker/{trackerId}
-----------------------------------------------------------------------------------------------


Delete a Tracker Profile Parcel for Service feature profile

.. code:: python

    def delete_tracker_profile_parcel_for_service(
        service_id: str, tracker_id: str
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
        client.v1.feature_profile.sdwan.service.tracker.delete_tracker_profile_parcel_for_service()


.. toctree::
    :maxdepth: 1

    schema/index

