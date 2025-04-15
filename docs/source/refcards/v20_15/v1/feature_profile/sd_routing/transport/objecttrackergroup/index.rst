==========================================================
v1.feature_profile.sd_routing.transport.objecttrackergroup
==========================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup
-----------------------------------------------------------------------------------------------------


Create a SD-Routing Object Tracker Group Feature for Transport Feature Profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateSdroutingTransportObjectTrackerGroupFeaturePostRequest,
    ) -> (
        CreateSdroutingTransportObjectTrackerGroupFeaturePostResponse
    ): ...


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
        client.v1.feature_profile.sd_routing.transport.objecttrackergroup.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup/{objectTrackerGroupId}
---------------------------------------------------------------------------------------------------------------------------


Edit a SD-Routing Object Tracker Group Feature for Transport Feature Profile

.. code:: python

    def put(
        transport_id: str,
        object_tracker_group_id: str,
        payload: EditSdroutingTransportObjectTrackerGroupFeaturePutRequest,
    ) -> EditSdroutingTransportObjectTrackerGroupFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.objecttrackergroup.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup/{objectTrackerGroupId}
------------------------------------------------------------------------------------------------------------------------------


Delete a SD-Routing Object Tracker Group Feature for Transport Feature Profile

.. code:: python

    def delete(
        transport_id: str, object_tracker_group_id: str
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
        client.v1.feature_profile.sd_routing.transport.objecttrackergroup.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup
----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdRoutingTransportObjecttrackergroupPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.objecttrackergroup.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup/{objectTrackerGroupId}
---------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, object_tracker_group_id: str
    ) -> GetSingleSdRoutingTransportObjecttrackergroupPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.objecttrackergroup.get()


.. toctree::
    :maxdepth: 1

    models

