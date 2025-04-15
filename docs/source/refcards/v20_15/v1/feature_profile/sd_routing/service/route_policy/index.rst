==================================================
v1.feature_profile.sd_routing.service.route_policy
==================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/route-policy
-------------------------------------------------------------------------------------------


Create a SD-Routing Route Policy Feature for Service Feature Profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateSdroutingServiceRoutePolicyFeaturePostRequest,
    ) -> CreateSdroutingServiceRoutePolicyFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.route_policy.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/route-policy/{routePolicyId}
----------------------------------------------------------------------------------------------------------


Edit a SD-Routing Route Policy Feature for Service Feature Profile

.. code:: python

    def put(
        service_id: str,
        route_policy_id: str,
        payload: EditSdroutingServiceRoutePolicyFeaturePutRequest,
    ) -> EditSdroutingServiceRoutePolicyFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.route_policy.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/route-policy/{routePolicyId}
-------------------------------------------------------------------------------------------------------------


Delete a SD-Routing Route Policy Feature for Service Feature Profile

.. code:: python

    def delete(service_id: str, route_policy_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.route_policy.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/route-policy
------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
    ) -> GetListSdRoutingServiceRoutePolicyPayload: ...


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
        client.v1.feature_profile.sd_routing.service.route_policy.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/route-policy/{routePolicyId}
----------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, route_policy_id: str
    ) -> GetSingleSdRoutingServiceRoutePolicyPayload: ...


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
        client.v1.feature_profile.sd_routing.service.route_policy.get()


.. toctree::
    :maxdepth: 1

    models

