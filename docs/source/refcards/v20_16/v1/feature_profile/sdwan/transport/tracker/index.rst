==========================================
v1.feature_profile.sdwan.transport.tracker
==========================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/tracker
------------------------------------------------------------------------------------


Get Tracker Profile Parcels for Transport feature profile

.. code:: python

    def get_tracker_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.tracker.get_tracker_profile_parcel_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/tracker
-------------------------------------------------------------------------------------


Create a Tracker Profile Parcel for Transport feature profile

.. code:: python

    def create_tracker_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.tracker.create_tracker_profile_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/tracker/{trackerId}
------------------------------------------------------------------------------------------------


Get Tracker Profile Parcel by parcelId for Transport feature profile

.. code:: python

    def get_tracker_profile_parcel_by_parcel_id_for_transport(
        transport_id: str, tracker_id: str
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
        client.v1.feature_profile.sdwan.transport.tracker.get_tracker_profile_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/tracker/{trackerId}
------------------------------------------------------------------------------------------------


Update a Tracker Profile Parcel for Transport feature profile

.. code:: python

    def edit_tracker_profile_parcel_for_transport(
        transport_id: str, tracker_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.transport.tracker.edit_tracker_profile_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/tracker/{trackerId}
---------------------------------------------------------------------------------------------------


Delete a Tracker Profile Parcel for Transport feature profile

.. code:: python

    def delete_tracker_profile_parcel_for_transport(
        transport_id: str, tracker_id: str
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
        client.v1.feature_profile.sdwan.transport.tracker.delete_tracker_profile_parcel_for_transport()


.. toctree::
    :maxdepth: 1

    schema/index

