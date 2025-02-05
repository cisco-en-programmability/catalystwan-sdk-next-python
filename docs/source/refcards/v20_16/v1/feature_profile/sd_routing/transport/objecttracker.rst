=====================================================
v1.feature_profile.sd_routing.transport.objecttracker
=====================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttracker
-----------------------------------------------------------------------------------------------


Get all SD-Routing object tracker features from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_object_tracker_features(
        transport_id: str,
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
        client.v1.feature_profile.sd_routing.transport.objecttracker.get_sdrouting_transport_object_tracker_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttracker
------------------------------------------------------------------------------------------------


Create a SD-Routing object tracker feature from a specific transport feature profile

.. code:: python

    def create_sdrouting_transport_object_tracker_feature(
        transport_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.transport.objecttracker.create_sdrouting_transport_object_tracker_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttracker/{objectTrackerId}
-----------------------------------------------------------------------------------------------------------------


Get the SD-Routing object tracker feature from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_object_tracker_feature(
        transport_id: str, object_tracker_id: str
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
        client.v1.feature_profile.sd_routing.transport.objecttracker.get_sdrouting_transport_object_tracker_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttracker/{objectTrackerId}
-----------------------------------------------------------------------------------------------------------------


Edit the SD-Routing object tracker feature from a specific transport feature profile

.. code:: python

    def edit_sdrouting_transport_object_tracker_feature(
        transport_id: str,
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
        client.v1.feature_profile.sd_routing.transport.objecttracker.edit_sdrouting_transport_object_tracker_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttracker/{objectTrackerId}
--------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing object tracker feature from a specific transport feature profile

.. code:: python

    def delete_sdrouting_transport_object_tracker_feature(
        transport_id: str, object_tracker_id: str
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
        client.v1.feature_profile.sd_routing.transport.objecttracker.delete_sdrouting_transport_object_tracker_feature()


