=======================================================
v1.feature_profile.sd_routing.service.vrf.routing.eigrp
=======================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp
-----------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
    ) -> GetListSdRoutingServiceVrfRoutingEigrpPayload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp/{eigrpId}
---------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, eigrp_id: str
    ) -> GetSingleSdRoutingServiceVrfRoutingEigrpPayload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/eigrp
-------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str
    ) -> List[GetServiceVrfAssociatedRoutingEigrpFeaturesGetResponse]: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/eigrp/{eigrpId}
-----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str, eigrp_id: str
    ) -> GetSingleSdRoutingServiceVrfVrfRoutingEigrpPayload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.get()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp
------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def post(
        service_id: str,
        payload: CreateSdroutingServiceVrfEigrpFeaturePostRequest,
    ) -> CreateSdroutingServiceVrfEigrpFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.post()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/eigrp
--------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def post(
        service_id: str,
        payload: CreateServiceVrfAndRoutingEigrpFeatureAssociationPostRequest,
        vrf_id: str,
    ) -> (
        CreateServiceVrfAndRoutingEigrpFeatureAssociationPostResponse
    ): ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp/{eigrpId}
---------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def put(
        service_id: str,
        eigrp_id: str,
        payload: EditSdroutingServiceVrfEigrpFeaturePutRequest,
    ) -> EditSdroutingServiceVrfEigrpFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.put()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/eigrp/{eigrpId}
-----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def put(
        service_id: str,
        eigrp_id: str,
        payload: EditServiceVrfAndRoutingEigrpFeatureAssociationPutRequest,
        vrf_id: str,
    ) -> EditServiceVrfAndRoutingEigrpFeatureAssociationPutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/eigrp/{eigrpId}
------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def delete(service_id: str, eigrp_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.delete()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/eigrp/{eigrpId}
--------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def delete(service_id: str, eigrp_id: str, vrf_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.eigrp.delete()


.. toctree::
    :maxdepth: 1

    models

