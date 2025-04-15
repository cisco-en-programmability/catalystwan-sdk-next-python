===============================================================
v1.feature_profile.sd_routing.transport.global_vrf.routing.ospf
===============================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospf
------------------------------------------------------------------------------------------------------------------


Associate an OSPF feature with the global VRF feature for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vrf_id: str,
        payload: CreateTransportGlobalVrfAndRoutingOspfParcelAssociationPostRequest,
    ) -> CreateTransportGlobalVrfAndRoutingOspfParcelAssociationPostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.ospf.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospf/{ospfId}
--------------------------------------------------------------------------------------------------------------------------


Replace the OSPF feature for the global VRF feature in transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vrf_id: str,
        ospf_id: str,
        payload: EditTransportGlobalVrfAndRoutingOspfFeatureAssociationPutRequest,
    ) -> (
        EditTransportGlobalVrfAndRoutingOspfFeatureAssociationPutResponse
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.ospf.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospf/{ospfId}
-----------------------------------------------------------------------------------------------------------------------------


Delete the global VRF and the OSPF feature association for transport feature profile

.. code:: python

    def delete(transport_id: str, vrf_id: str, ospf_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.ospf.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospf
-----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str
    ) -> List[
        GetTransportVrfAssociatedRoutingOspfFeaturesGetResponse
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.ospf.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospf/{ospfId}
--------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str, ospf_id: str
    ) -> GetSingleSdRoutingTransportGlobalVrfRoutingOspfPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.ospf.get()


.. toctree::
    :maxdepth: 1

    models

