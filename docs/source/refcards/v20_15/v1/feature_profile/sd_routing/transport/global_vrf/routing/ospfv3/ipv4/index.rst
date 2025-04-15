======================================================================
v1.feature_profile.sd_routing.transport.global_vrf.routing.ospfv3.ipv4
======================================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv4
-------------------------------------------------------------------------------------------------------------------------


Associate an OSPFv3 IPv4 feature with the global VRF feature for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vrf_id: str,
        payload: CreateTransportGlobalVrfAndRoutingOspfv3Ipv4FeatureAssociationPostRequest,
    ) -> CreateTransportGlobalVrfAndRoutingOspfv3Ipv4FeatureAssociationPostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.ospfv3.ipv4.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv4/{ospfv3Id}
-----------------------------------------------------------------------------------------------------------------------------------


Replace the OSPFv3 IPv4 feature for the global VRF feature in transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vrf_id: str,
        ospfv3_id: str,
        payload: EditTransportGlobalVrfAndRoutingOspfv3Ipv4FeatureAssociationPutRequest,
    ) -> EditTransportGlobalVrfAndRoutingOspfv3Ipv4FeatureAssociationPutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.ospfv3.ipv4.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv4/{ospfv3Id}
--------------------------------------------------------------------------------------------------------------------------------------


Delete the global VRF and the OSPFv3 IPv4 feature association for transport feature profile

.. code:: python

    def delete(
        transport_id: str, vrf_id: str, ospfv3_id: str
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.ospfv3.ipv4.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv4
------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str
    ) -> List[
        GetTransportVrfAssociatedRoutingOspfv3Ipv4FeaturesGetResponse
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.ospfv3.ipv4.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv4/{ospfv3Id}
-----------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str, ospfv3_id: str
    ) -> GetSingleSdRoutingTransportGlobalVrfRoutingOspfv3Ipv4Payload: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.ospfv3.ipv4.get()


.. toctree::
    :maxdepth: 1

    models

