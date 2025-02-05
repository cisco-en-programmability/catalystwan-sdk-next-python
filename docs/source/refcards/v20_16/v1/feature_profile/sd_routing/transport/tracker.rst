===============================================
v1.feature_profile.sd_routing.transport.tracker
===============================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/tracker
-----------------------------------------------------------------------------------------


Get Tracker Profile Features for Transport feature profile

.. code:: python

    def get_tracker_profile_parcel_for_transport_1(
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
        client.v1.feature_profile.sd_routing.transport.tracker.get_tracker_profile_parcel_for_transport_1()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/tracker
------------------------------------------------------------------------------------------


Create a Tracker Profile Feature for Transport feature profile

.. code:: python

    def create_tracker_profile_parcel_for_transport_1(
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
        client.v1.feature_profile.sd_routing.transport.tracker.create_tracker_profile_parcel_for_transport_1()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/tracker/{trackerId}
-----------------------------------------------------------------------------------------------------


Get Tracker Profile Feature by parcelId for Transport feature profile

.. code:: python

    def get_tracker_profile_parcel_by_parcel_id_for_transport_1(
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
        client.v1.feature_profile.sd_routing.transport.tracker.get_tracker_profile_parcel_by_parcel_id_for_transport_1()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/tracker/{trackerId}
-----------------------------------------------------------------------------------------------------


Update a Tracker Profile Feature for Transport feature profile

.. code:: python

    def edit_tracker_profile_parcel_for_transport_1(
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
        client.v1.feature_profile.sd_routing.transport.tracker.edit_tracker_profile_parcel_for_transport_1()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------------------


Delete a Tracker Profile Feature for Transport feature profile

.. code:: python

    def delete_tracker_profile_parcel_for_transport_1(
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
        client.v1.feature_profile.sd_routing.transport.tracker.delete_tracker_profile_parcel_for_transport_1()


