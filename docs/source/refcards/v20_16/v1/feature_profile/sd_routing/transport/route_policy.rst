====================================================
v1.feature_profile.sd_routing.transport.route_policy
====================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/route-policy
----------------------------------------------------------------------------------------------


Get all SD-Routing route policy features from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_route_policy_features(
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
        client.v1.feature_profile.sd_routing.transport.route_policy.get_sdrouting_transport_route_policy_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/route-policy
-----------------------------------------------------------------------------------------------


Create a SD-Routing route policy feature from a specific transport feature profile

.. code:: python

    def create_sdrouting_transport_route_policy_feature(
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
        client.v1.feature_profile.sd_routing.transport.route_policy.create_sdrouting_transport_route_policy_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/route-policy/{routePolicyId}
--------------------------------------------------------------------------------------------------------------


Get the SD-Routing route policy feature from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_route_policy_feature(
        transport_id: str, route_policy_id: str
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
        client.v1.feature_profile.sd_routing.transport.route_policy.get_sdrouting_transport_route_policy_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/route-policy/{routePolicyId}
--------------------------------------------------------------------------------------------------------------


Edit the SD-Routing route policy feature from a specific transport feature profile

.. code:: python

    def edit_sdrouting_transport_route_policy_feature(
        transport_id: str,
        route_policy_id: str,
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
        client.v1.feature_profile.sd_routing.transport.route_policy.edit_sdrouting_transport_route_policy_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/route-policy/{routePolicyId}
-----------------------------------------------------------------------------------------------------------------


Delete the SD-Routing route policy feature from a specific transport feature profile

.. code:: python

    def delete_sdrouting_transport_route_policy_feature(
        transport_id: str, route_policy_id: str
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
        client.v1.feature_profile.sd_routing.transport.route_policy.delete_sdrouting_transport_route_policy_feature()


