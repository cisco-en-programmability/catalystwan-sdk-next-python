========================================
v1.feature_profile.sdwan.service.tracker
========================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/tracker
---------------------------------------------------------------------------------


Create a Tracker Profile Parcel for Service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateTrackerProfileParcelForServicePostRequest,
    ) -> CreateTrackerProfileParcelForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.tracker.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------


Update a Tracker Profile Parcel for Service feature profile

.. code:: python

    def put(
        service_id: str,
        tracker_id: str,
        payload: EditTrackerProfileParcelForServicePutRequest,
    ) -> EditTrackerProfileParcelForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.tracker.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/tracker/{trackerId}
-----------------------------------------------------------------------------------------------


Delete a Tracker Profile Parcel for Service feature profile

.. code:: python

    def delete(service_id: str, tracker_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.tracker.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/tracker
--------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(service_id: str) -> GetListSdwanServiceTrackerPayload: ...


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
        client.v1.feature_profile.sdwan.service.tracker.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, tracker_id: str
    ) -> GetSingleSdwanServiceTrackerPayload: ...


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
        client.v1.feature_profile.sdwan.service.tracker.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

