====================================================
v1.feature_profile.sd_routing.transport.route_policy
====================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/route-policy
-----------------------------------------------------------------------------------------------


Create a SD-Routing Route Policy Feature for Transport Feature Profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateSdroutingTransportRoutePolicyFeaturePostRequest,
    ) -> CreateSdroutingTransportRoutePolicyFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.route_policy.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/route-policy/{routePolicyId}
--------------------------------------------------------------------------------------------------------------


Edit a SD-Routing Route Policy Feature for Transport Feature Profile

.. code:: python

    def put(
        transport_id: str,
        route_policy_id: str,
        payload: EditSdroutingTransportRoutePolicyFeaturePutRequest,
    ) -> EditSdroutingTransportRoutePolicyFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.route_policy.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/route-policy/{routePolicyId}
-----------------------------------------------------------------------------------------------------------------


Delete a SD-Routing Route Policy Feature for Transport Feature Profile

.. code:: python

    def delete(transport_id: str, route_policy_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.transport.route_policy.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/route-policy
----------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdRoutingTransportRoutePolicyPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.route_policy.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/route-policy/{routePolicyId}
--------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, route_policy_id: str
    ) -> GetSingleSdRoutingTransportRoutePolicyPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.route_policy.get()


.. toctree::
    :maxdepth: 1

    models

