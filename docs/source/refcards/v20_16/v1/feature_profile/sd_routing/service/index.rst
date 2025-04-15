=====================================
v1.feature_profile.sd_routing.service
=====================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service
------------------------------------------------------------------


Create a SD-Routing Service Feature Profile

.. code:: python

    def post(
        payload: CreateSdroutingServiceFeatureProfilePostRequest,
    ) -> CreateSdroutingServiceFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}
-----------------------------------------------------------------------------


Edit a SD-Routing Service Feature Profile

.. code:: python

    def put(
        service_id: str,
        payload: EditSdroutingServiceFeatureProfilePutRequest,
    ) -> EditSdroutingServiceFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}
--------------------------------------------------------------------------------


Delete a SD-Routing Service Feature Profile

.. code:: python

    def delete(service_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service
-----------------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> List[GetSdroutingServiceFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.sd_routing.service.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}
-----------------------------------------------------------------------------


.. code:: python

    @overload
    def get(service_id: str) -> GetSingleSdRoutingServicePayload: ...


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
        client.v1.feature_profile.sd_routing.service.get()


.. toctree::
    :maxdepth: 1

    dhcp_server/index
    ipsec_profile/index
    ipv4_acl/index
    multicloud_connection/index
    objecttracker/index
    objecttrackergroup/index
    route_policy/index
    routing/index
    vrf/index
    models

