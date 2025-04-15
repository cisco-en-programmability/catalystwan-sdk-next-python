=====================================================
v1.feature_profile.sd_routing.transport.objecttracker
=====================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttracker
------------------------------------------------------------------------------------------------


Create a SD-Routing Object Tracker Feature for Transport Feature Profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateSdroutingTransportObjectTrackerFeaturePostRequest,
    ) -> CreateSdroutingTransportObjectTrackerFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.objecttracker.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttracker/{objectTrackerId}
-----------------------------------------------------------------------------------------------------------------


Edit a SD-Routing Object Tracker Feature for Transport Feature Profile

.. code:: python

    def put(
        transport_id: str,
        object_tracker_id: str,
        payload: EditSdroutingTransportObjectTrackerFeaturePutRequest,
    ) -> EditSdroutingTransportObjectTrackerFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.objecttracker.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttracker/{objectTrackerId}
--------------------------------------------------------------------------------------------------------------------


Delete a SD-Routing Object Tracker Feature for Transport Feature Profile

.. code:: python

    def delete(transport_id: str, object_tracker_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.transport.objecttracker.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttracker
-----------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdRoutingTransportObjecttrackerPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.objecttracker.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttracker/{objectTrackerId}
-----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, object_tracker_id: str
    ) -> GetSingleSdRoutingTransportObjecttrackerPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.objecttracker.get()


.. toctree::
    :maxdepth: 1

    models

