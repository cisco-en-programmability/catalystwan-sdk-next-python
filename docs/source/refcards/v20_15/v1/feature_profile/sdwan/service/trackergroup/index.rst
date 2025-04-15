=============================================
v1.feature_profile.sdwan.service.trackergroup
=============================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/trackergroup
--------------------------------------------------------------------------------------


Create a TrackerGroup Profile Parcel for Service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateTrackerGroupProfileParcelForServicePostRequest,
    ) -> CreateTrackerGroupProfileParcelForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.trackergroup.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/trackergroup/{trackergroupId}
------------------------------------------------------------------------------------------------------


Update a TrackerGroup Profile Parcel for Service feature profile

.. code:: python

    def put(
        service_id: str,
        trackergroup_id: str,
        payload: EditTrackerGroupProfileParcelForServicePutRequest,
    ) -> EditTrackerGroupProfileParcelForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.trackergroup.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/trackergroup/{trackergroupId}
---------------------------------------------------------------------------------------------------------


Delete a TrackerGroup Profile Parcel for Service feature profile

.. code:: python

    def delete(service_id: str, trackergroup_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.trackergroup.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/trackergroup
-------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
    ) -> GetListSdwanServiceTrackergroupPayload: ...


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
        client.v1.feature_profile.sdwan.service.trackergroup.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/trackergroup/{trackergroupId}
------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, trackergroup_id: str
    ) -> GetSingleSdwanServiceTrackergroupPayload: ...


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
        client.v1.feature_profile.sdwan.service.trackergroup.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

