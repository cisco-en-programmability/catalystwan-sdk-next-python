=======================================================
v1.feature_profile.sd_routing.transport.vrf.routing.bgp
=======================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/routing/bgp
-------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdRoutingTransportVrfRoutingBgpPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/routing/bgp/{bgpId}
---------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, bgp_id: str
    ) -> GetSingleSdRoutingTransportVrfRoutingBgpPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/bgp
---------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str
    ) -> List[
        GetTransportVrfAssociatedRoutingBgpFeatures1GetResponse
    ]: ...


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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/bgp/{bgpId}
-----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str, bgp_id: str
    ) -> GetSingleSdRoutingTransportVrfVrfRoutingBgpPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.get()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/routing/bgp
--------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def post(
        transport_id: str,
        payload: CreateSdroutingTransportVrfBgpFeaturePostRequest,
    ) -> CreateSdroutingTransportVrfBgpFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.post()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/bgp
----------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def post(
        transport_id: str,
        payload: CreateTransportVrfAndRoutingBgpFeatureAssociationPostRequest,
        vrf_id: str,
    ) -> (
        CreateTransportVrfAndRoutingBgpFeatureAssociationPostResponse
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/routing/bgp/{bgpId}
---------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def put(
        transport_id: str,
        bgp_id: str,
        payload: EditSdroutingTransportVrfBgpFeaturePutRequest,
    ) -> EditSdroutingTransportVrfBgpFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.put()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/bgp/{bgpId}
-----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def put(
        transport_id: str,
        bgp_id: str,
        payload: EditTransportVrfAndRoutingBgpFeatureAssociationPutRequest,
        vrf_id: str,
    ) -> EditTransportVrfAndRoutingBgpFeatureAssociationPutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/routing/bgp/{bgpId}
------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def delete(transport_id: str, bgp_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.delete()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/bgp/{bgpId}
--------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def delete(transport_id: str, bgp_id: str, vrf_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.delete()


.. toctree::
    :maxdepth: 1

    models

