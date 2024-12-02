==================================================
v1.feature_profile.sd_routing.service.route_policy
==================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/route-policy
------------------------------------------------------------------------------------------


Get all SD-Routing route policy features from a specific service feature profile

.. code:: python

    def get_sdrouting_service_route_policy_features(
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
        client.v1.feature_profile.sd_routing.service.route_policy.get_sdrouting_service_route_policy_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/route-policy
-------------------------------------------------------------------------------------------


Create a SD-Routing route policy feature from a specific service feature profile

.. code:: python

    def create_sdrouting_service_route_policy_feature(
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
        client.v1.feature_profile.sd_routing.service.route_policy.create_sdrouting_service_route_policy_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/route-policy/{routePolicyId}
----------------------------------------------------------------------------------------------------------


Get the SD-Routing route policy feature from a specific service feature profile

.. code:: python

    def get_sdrouting_service_route_policy_feature(
        service_id: str, route_policy_id: str
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
        client.v1.feature_profile.sd_routing.service.route_policy.get_sdrouting_service_route_policy_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/route-policy/{routePolicyId}
----------------------------------------------------------------------------------------------------------


Edit the SD-Routing route policy feature from a specific service feature profile

.. code:: python

    def edit_sdrouting_service_route_policy_feature(
        service_id: str,
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
        client.v1.feature_profile.sd_routing.service.route_policy.edit_sdrouting_service_route_policy_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/route-policy/{routePolicyId}
-------------------------------------------------------------------------------------------------------------


Delete the SD-Routing route policy feature from a specific service feature profile

.. code:: python

    def delete_sdrouting_service_route_policy_feature(
        service_id: str, route_policy_id: str
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
        client.v1.feature_profile.sd_routing.service.route_policy.delete_sdrouting_service_route_policy_feature()


