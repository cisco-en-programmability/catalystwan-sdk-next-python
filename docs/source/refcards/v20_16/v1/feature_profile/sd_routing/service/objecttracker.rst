===================================================
v1.feature_profile.sd_routing.service.objecttracker
===================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/objecttracker
-------------------------------------------------------------------------------------------


Get all SD-Routing object tracker features from a specific service feature profile

.. code:: python

    def get_sdrouting_service_object_tracker_features(
        service_id: str,
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.service.objecttracker.get_sdrouting_service_object_tracker_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/objecttracker
--------------------------------------------------------------------------------------------


Create a SD-Routing object tracker feature from a specific service feature profile

.. code:: python

    def create_sdrouting_service_object_tracker_feature(
        service_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.service.objecttracker.create_sdrouting_service_object_tracker_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/objecttracker/{objectTrackerId}
-------------------------------------------------------------------------------------------------------------


Get the SD-Routing object tracker feature from a specific service feature profile

.. code:: python

    def get_sdrouting_service_object_tracker_feature(
        service_id: str, object_tracker_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.service.objecttracker.get_sdrouting_service_object_tracker_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/objecttracker/{objectTrackerId}
-------------------------------------------------------------------------------------------------------------


Edit the SD-Routing object tracker feature from a specific service feature profile

.. code:: python

    def edit_sdrouting_service_object_tracker_feature(
        service_id: str,
        object_tracker_id: str,
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.service.objecttracker.edit_sdrouting_service_object_tracker_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/objecttracker/{objectTrackerId}
----------------------------------------------------------------------------------------------------------------


Delete the SD-Routing object tracker feature from a specific service feature profile

.. code:: python

    def delete_sdrouting_service_object_tracker_feature(
        service_id: str, object_tracker_id: str
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
        client.v1.feature_profile.sd_routing.service.objecttracker.delete_sdrouting_service_object_tracker_feature()


