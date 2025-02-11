==========================================================
v1.feature_profile.sd_routing.transport.objecttrackergroup
==========================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup
----------------------------------------------------------------------------------------------------


Get all SD-Routing object tracker group features from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_object_tracker_group_features(
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
        client.v1.feature_profile.sd_routing.transport.objecttrackergroup.get_sdrouting_transport_object_tracker_group_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup
-----------------------------------------------------------------------------------------------------


Create a SD-Routing object tracker group feature from a specific transport feature profile

.. code:: python

    def create_sdrouting_transport_object_tracker_group_feature(
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
        client.v1.feature_profile.sd_routing.transport.objecttrackergroup.create_sdrouting_transport_object_tracker_group_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup/{objectTrackerGroupId}
---------------------------------------------------------------------------------------------------------------------------


Get the SD-Routing object tracker group feature from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_object_tracker_group_feature(
        transport_id: str, object_tracker_group_id: str
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
        client.v1.feature_profile.sd_routing.transport.objecttrackergroup.get_sdrouting_transport_object_tracker_group_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup/{objectTrackerGroupId}
---------------------------------------------------------------------------------------------------------------------------


Edit the SD-Routing object tracker group feature from a specific transport feature profile

.. code:: python

    def edit_sdrouting_transport_object_tracker_group_feature(
        transport_id: str,
        object_tracker_group_id: str,
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
        client.v1.feature_profile.sd_routing.transport.objecttrackergroup.edit_sdrouting_transport_object_tracker_group_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/objecttrackergroup/{objectTrackerGroupId}
------------------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing object tracker group feature from a specific transport feature profile

.. code:: python

    def delete_sdrouting_transport_object_tracker_group_feature(
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
        client.v1.feature_profile.sd_routing.transport.objecttrackergroup.delete_sdrouting_transport_object_tracker_group_feature()


