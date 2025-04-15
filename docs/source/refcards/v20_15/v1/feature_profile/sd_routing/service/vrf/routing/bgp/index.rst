=====================================================
v1.feature_profile.sd_routing.service.vrf.routing.bgp
=====================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp
---------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
    ) -> GetListSdRoutingServiceVrfRoutingBgpPayload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp/{bgpId}
-----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, bgp_id: str
    ) -> GetSingleSdRoutingServiceVrfRoutingBgpPayload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/bgp
-----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str
    ) -> List[GetServiceVrfAssociatedRoutingBgpFeaturesGetResponse]: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/bgp/{bgpId}
-------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str, bgp_id: str
    ) -> GetSingleSdRoutingServiceVrfVrfRoutingBgpPayload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.get()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp
----------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def post(
        service_id: str,
        payload: CreateSdroutingServiceVrfBgpFeaturePostRequest,
    ) -> CreateSdroutingServiceVrfBgpFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.post()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/bgp
------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def post(
        service_id: str,
        payload: CreateServiceVrfAndRoutingBgpFeatureAssociationPostRequest,
        vrf_id: str,
    ) -> CreateServiceVrfAndRoutingBgpFeatureAssociationPostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp/{bgpId}
-----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def put(
        service_id: str,
        bgp_id: str,
        payload: EditSdroutingServiceVrfBgpFeaturePutRequest,
    ) -> EditSdroutingServiceVrfBgpFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.put()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/bgp/{bgpId}
-------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def put(
        service_id: str,
        bgp_id: str,
        payload: EditServiceVrfAndRoutingBgpFeatureAssociationPutRequest,
        vrf_id: str,
    ) -> EditServiceVrfAndRoutingBgpFeatureAssociationPutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp/{bgpId}
--------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def delete(service_id: str, bgp_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.delete()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/bgp/{bgpId}
----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def delete(service_id: str, bgp_id: str, vrf_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.delete()


.. toctree::
    :maxdepth: 1

    models

