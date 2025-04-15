========================================================
v1.feature_profile.sd_routing.service.objecttrackergroup
========================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/objecttrackergroup
-------------------------------------------------------------------------------------------------


Create a SD-Routing object tracker group feature from a specific service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateSdroutingServiceObjectTrackerGroupFeaturePostRequest,
    ) -> CreateSdroutingServiceObjectTrackerGroupFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.objecttrackergroup.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/objecttrackergroup/{objectTrackerGroupId}
-----------------------------------------------------------------------------------------------------------------------


Edit the SD-Routing object tracker group feature from a specific service feature profile

.. code:: python

    def put(
        service_id: str,
        object_tracker_group_id: str,
        payload: EditSdroutingServiceObjectTrackerGroupFeaturePutRequest,
    ) -> EditSdroutingServiceObjectTrackerGroupFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.objecttrackergroup.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/objecttrackergroup/{objectTrackerGroupId}
--------------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing object tracker group feature from a specific service feature profile

.. code:: python

    def delete(service_id: str, object_tracker_group_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.objecttrackergroup.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/objecttrackergroup
------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
    ) -> GetListSdRoutingServiceObjecttrackergroupPayload: ...


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
        client.v1.feature_profile.sd_routing.service.objecttrackergroup.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/objecttrackergroup/{objectTrackerGroupId}
-----------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, object_tracker_group_id: str
    ) -> GetSingleSdRoutingServiceObjecttrackergroupPayload: ...


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
        client.v1.feature_profile.sd_routing.service.objecttrackergroup.get()


.. toctree::
    :maxdepth: 1

    models

