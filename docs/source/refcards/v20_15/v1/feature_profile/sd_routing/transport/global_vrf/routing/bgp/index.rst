==============================================================
v1.feature_profile.sd_routing.transport.global_vrf.routing.bgp
==============================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/routing/bgp
--------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdRoutingTransportGlobalVrfRoutingBgpPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.bgp.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/routing/bgp/{bgpId}
----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, bgp_id: str
    ) -> GetSingleSdRoutingTransportGlobalVrfRoutingBgpPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.bgp.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/bgp
----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str
    ) -> List[GetTransportVrfAssociatedRoutingBgpFeaturesGetResponse]: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.bgp.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/bgp/{bgpId}
------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str, bgp_id: str
    ) -> (
        GetSingleSdRoutingTransportGlobalVrfGlobalVrfRoutingBgpPayload
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.bgp.get()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/routing/bgp
---------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def post(
        transport_id: str,
        payload: CreateSdroutingTransportGlobalVrfBgpFeaturePostRequest,
    ) -> CreateSdroutingTransportGlobalVrfBgpFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.bgp.post()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/bgp
-----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def post(
        transport_id: str,
        payload: CreateTransportGlobalVrfAndRoutingBgpFeatureAssociationPostRequest,
        vrf_id: str,
    ) -> CreateTransportGlobalVrfAndRoutingBgpFeatureAssociationPostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.bgp.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/routing/bgp/{bgpId}
----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def put(
        transport_id: str,
        bgp_id: str,
        payload: EditSdroutingTransportGlobalVrfBgpFeaturePutRequest,
    ) -> EditSdroutingTransportGlobalVrfBgpFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.bgp.put()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/bgp/{bgpId}
------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def put(
        transport_id: str,
        bgp_id: str,
        payload: EditTransportGlobalVrfAndRoutingBgpFeatureAssociationPutRequest,
        vrf_id: str,
    ) -> (
        EditTransportGlobalVrfAndRoutingBgpFeatureAssociationPutResponse
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.bgp.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/routing/bgp/{bgpId}
-------------------------------------------------------------------------------------------------------------------


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.bgp.delete()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/bgp/{bgpId}
---------------------------------------------------------------------------------------------------------------------------


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.bgp.delete()


.. toctree::
    :maxdepth: 1

    models

