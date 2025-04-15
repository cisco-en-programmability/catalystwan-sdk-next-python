====================================================
v1.feature_profile.sd_routing.transport.trackergroup
====================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/trackergroup
-----------------------------------------------------------------------------------------------


Create a TrackerGroup Profile Feature for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateTrackerGroupProfileParcelForTransport1PostRequest,
    ) -> CreateTrackerGroupProfileParcelForTransport1PostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.trackergroup.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/trackergroup/{trackergroupId}
---------------------------------------------------------------------------------------------------------------


Update a TrackerGroup Profile Feature for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        trackergroup_id: str,
        payload: EditTrackerGroupProfileParcelForTransport1PutRequest,
    ) -> EditTrackerGroupProfileParcelForTransport1PutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.trackergroup.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/trackergroup/{trackergroupId}
------------------------------------------------------------------------------------------------------------------


Delete a TrackerGroup Profile Feature for Transport feature profile

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
        client.v1.feature_profile.sd_routing.transport.trackergroup.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/trackergroup
----------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdRoutingTransportTrackergroupPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.trackergroup.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/trackergroup/{trackergroupId}
---------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, trackergroup_id: str
    ) -> GetSingleSdRoutingTransportTrackergroupPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.trackergroup.get()


.. toctree::
    :maxdepth: 1

    models

