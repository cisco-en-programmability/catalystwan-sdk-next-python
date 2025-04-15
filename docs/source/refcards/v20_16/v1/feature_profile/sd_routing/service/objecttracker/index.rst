===================================================
v1.feature_profile.sd_routing.service.objecttracker
===================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/objecttracker
--------------------------------------------------------------------------------------------


Create a SD-Routing object tracker feature from a specific service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateSdroutingServiceObjectTrackerFeaturePostRequest,
    ) -> CreateSdroutingServiceObjectTrackerFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.objecttracker.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/objecttracker/{objectTrackerId}
-------------------------------------------------------------------------------------------------------------


Edit the SD-Routing object tracker feature from a specific service feature profile

.. code:: python

    def put(
        service_id: str,
        object_tracker_id: str,
        payload: EditSdroutingServiceObjectTrackerFeaturePutRequest,
    ) -> EditSdroutingServiceObjectTrackerFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.objecttracker.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/objecttracker/{objectTrackerId}
----------------------------------------------------------------------------------------------------------------


Delete the SD-Routing object tracker feature from a specific service feature profile

.. code:: python

    def delete(service_id: str, object_tracker_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.objecttracker.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/objecttracker
-------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
    ) -> GetListSdRoutingServiceObjecttrackerPayload: ...


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
        client.v1.feature_profile.sd_routing.service.objecttracker.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/objecttracker/{objectTrackerId}
-------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, object_tracker_id: str
    ) -> GetSingleSdRoutingServiceObjecttrackerPayload: ...


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
        client.v1.feature_profile.sd_routing.service.objecttracker.get()


.. toctree::
    :maxdepth: 1

    models

