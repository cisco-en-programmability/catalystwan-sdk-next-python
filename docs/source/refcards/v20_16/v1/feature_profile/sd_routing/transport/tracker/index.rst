===============================================
v1.feature_profile.sd_routing.transport.tracker
===============================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/tracker
------------------------------------------------------------------------------------------


Create a Tracker Profile Feature for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateTrackerProfileParcelForTransport1PostRequest,
    ) -> CreateTrackerProfileParcelForTransport1PostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.tracker.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/tracker/{trackerId}
-----------------------------------------------------------------------------------------------------


Update a Tracker Profile Feature for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        tracker_id: str,
        payload: EditTrackerProfileParcelForTransport1PutRequest,
    ) -> EditTrackerProfileParcelForTransport1PutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.tracker.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------------------


Delete a Tracker Profile Feature for Transport feature profile

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
        client.v1.feature_profile.sd_routing.transport.tracker.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/tracker
-----------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdRoutingTransportTrackerPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.tracker.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/tracker/{trackerId}
-----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, tracker_id: str
    ) -> GetSingleSdRoutingTransportTrackerPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.tracker.get()


.. toctree::
    :maxdepth: 1

    models

