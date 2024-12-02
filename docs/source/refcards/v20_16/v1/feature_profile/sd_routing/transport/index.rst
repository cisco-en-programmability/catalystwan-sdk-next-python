=======================================
v1.feature_profile.sd_routing.transport
=======================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport
-------------------------------------------------------------------


Get all SD-Routing Transport Feature Profiles

.. code:: python

    def get_sdrouting_transport_feature_profiles(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> Any: ...


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
        client.v1.feature_profile.sd_routing.transport.get_sdrouting_transport_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport
--------------------------------------------------------------------


Create a SD-Routing Transport Feature Profile

.. code:: python

    def create_sdrouting_transport_feature_profile(
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
        client.v1.feature_profile.sd_routing.transport.create_sdrouting_transport_feature_profile()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}
---------------------------------------------------------------------------------


Get a SD-Routing Transport Feature Profile

.. code:: python

    def get_sdrouting_transport_feature_profile(
        transport_id: str,
    ) -> Any: ...


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
        client.v1.feature_profile.sd_routing.transport.get_sdrouting_transport_feature_profile()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}
---------------------------------------------------------------------------------


Edit a SD-Routing Transport Feature Profile

.. code:: python

    def edit_sdrouting_transport_feature_profile(
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
        client.v1.feature_profile.sd_routing.transport.edit_sdrouting_transport_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}
------------------------------------------------------------------------------------


Delete a SD-Routing Transport Feature Profile

.. code:: python

    def delete_sdrouting_transport_feature_profile(
        transport_id: str,
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
        client.v1.feature_profile.sd_routing.transport.delete_sdrouting_transport_feature_profile()


.. toctree::
    :maxdepth: 1

    cellular_controller/index
    cellular_profile
    global_vrf/index
    gps
    ipv4_acl
    management_vrf/index
    multicloud_connection
    objecttracker
    objecttrackergroup
    route_policy
    routing/index
    tracker
    trackergroup
    vrf/index

