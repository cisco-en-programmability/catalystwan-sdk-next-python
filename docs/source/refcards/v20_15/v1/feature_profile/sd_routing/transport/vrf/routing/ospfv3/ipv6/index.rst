===============================================================
v1.feature_profile.sd_routing.transport.vrf.routing.ospfv3.ipv6
===============================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospfv3/ipv6
------------------------------------------------------------------------------------------------------------------


Associate an OSPFv3 IPv6 feature with the WAN VRF feature for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vrf_id: str,
        payload: CreateTransportVrfAndRoutingOspfv3Ipv6FeatureAssociationPostRequest,
    ) -> CreateTransportVrfAndRoutingOspfv3Ipv6FeatureAssociationPostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.ospfv3.ipv6.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospfv3/ipv6/{ospfv3Id}
----------------------------------------------------------------------------------------------------------------------------


Replace the OSPFv3 IPv6 feature for the WAN VRF feature in transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vrf_id: str,
        ospfv3_id: str,
        payload: EditTransportVrfAndRoutingOspfv3Ipv6FeatureAssociationPutRequest,
    ) -> (
        EditTransportVrfAndRoutingOspfv3Ipv6FeatureAssociationPutResponse
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.ospfv3.ipv6.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospfv3/ipv6/{ospfv3Id}
-------------------------------------------------------------------------------------------------------------------------------


Delete the WAN VRF feature and OSPFv3 IPv6 feature association for transport feature profile

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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.ospfv3.ipv6.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospfv3/ipv6
-----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str
    ) -> List[
        GetTransportVrfAssociatedRoutingOspfv3Ipv6Features1GetResponse
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.ospfv3.ipv6.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospfv3/ipv6/{ospfv3Id}
----------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str, ospfv3_id: str
    ) -> GetSingleSdRoutingTransportVrfRoutingOspfv3Ipv6Payload: ...


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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.ospfv3.ipv6.get()


.. toctree::
    :maxdepth: 1

    models

