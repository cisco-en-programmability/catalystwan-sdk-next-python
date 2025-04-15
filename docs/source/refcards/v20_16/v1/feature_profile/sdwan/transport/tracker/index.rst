==========================================
v1.feature_profile.sdwan.transport.tracker
==========================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/tracker
-------------------------------------------------------------------------------------


Create a Tracker Profile Parcel for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateTrackerProfileParcelForTransportPostRequest,
    ) -> CreateTrackerProfileParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.tracker.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/tracker/{trackerId}
------------------------------------------------------------------------------------------------


Update a Tracker Profile Parcel for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        tracker_id: str,
        payload: EditTrackerProfileParcelForTransportPutRequest,
    ) -> EditTrackerProfileParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.tracker.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/tracker/{trackerId}
---------------------------------------------------------------------------------------------------


Delete a Tracker Profile Parcel for Transport feature profile

.. code:: python

    def delete(transport_id: str, tracker_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.tracker.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/tracker
------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(transport_id: str) -> GetListSdwanTransportTrackerPayload: ...


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
        client.v1.feature_profile.sdwan.transport.tracker.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/tracker/{trackerId}
------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, tracker_id: str
    ) -> GetSingleSdwanTransportTrackerPayload: ...


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
        client.v1.feature_profile.sdwan.transport.tracker.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

