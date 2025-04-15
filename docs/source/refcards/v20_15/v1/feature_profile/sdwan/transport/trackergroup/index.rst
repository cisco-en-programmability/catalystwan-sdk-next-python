===============================================
v1.feature_profile.sdwan.transport.trackergroup
===============================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/trackergroup
------------------------------------------------------------------------------------------


Create a TrackerGroup Profile Parcel for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateTrackerGroupProfileParcelForTransportPostRequest,
    ) -> CreateTrackerGroupProfileParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.trackergroup.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/trackergroup/{trackergroupId}
----------------------------------------------------------------------------------------------------------


Update a TrackerGroup Profile Parcel for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        trackergroup_id: str,
        payload: EditTrackerGroupProfileParcelForTransportPutRequest,
    ) -> EditTrackerGroupProfileParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.trackergroup.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/trackergroup/{trackergroupId}
-------------------------------------------------------------------------------------------------------------


Delete a TrackerGroup Profile Parcel for Transport feature profile

.. code:: python

    def delete(transport_id: str, trackergroup_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.trackergroup.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/trackergroup
-----------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdwanTransportTrackergroupPayload: ...


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
        client.v1.feature_profile.sdwan.transport.trackergroup.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/trackergroup/{trackergroupId}
----------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, trackergroup_id: str
    ) -> GetSingleSdwanTransportTrackergroupPayload: ...


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
        client.v1.feature_profile.sdwan.transport.trackergroup.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

