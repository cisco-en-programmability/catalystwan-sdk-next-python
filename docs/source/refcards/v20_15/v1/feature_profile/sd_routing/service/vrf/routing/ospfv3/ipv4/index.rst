=============================================================
v1.feature_profile.sd_routing.service.vrf.routing.ospfv3.ipv4
=============================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4
--------------------------------------------------------------------------------------------------------------


Associate an OSPFv3 IPv4 feature with the LAN VRF feature for service feature profile

.. code:: python

    def post(
        service_id: str,
        vrf_id: str,
        payload: CreateServiceVrfAndRoutingOspfv3Ipv4FeatureAssociationPostRequest,
    ) -> (
        CreateServiceVrfAndRoutingOspfv3Ipv4FeatureAssociationPostResponse
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospfv3.ipv4.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4/{ospfv3Id}
------------------------------------------------------------------------------------------------------------------------


Replace the OSPFv3 IPv4 feature for LAN VRF feature in service feature profile

.. code:: python

    def put(
        service_id: str,
        vrf_id: str,
        ospfv3_id: str,
        payload: EditServiceVrfAndRoutingOspfv3Ipv4FeatureAssociationPutRequest,
    ) -> (
        EditServiceVrfAndRoutingOspfv3Ipv4FeatureAssociationPutResponse
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospfv3.ipv4.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4/{ospfv3Id}
---------------------------------------------------------------------------------------------------------------------------


Delete the VRF feature and OSPFv3 IPv4 feature association for service feature profile

.. code:: python

    def delete(service_id: str, vrf_id: str, ospfv3_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospfv3.ipv4.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4
-------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str
    ) -> List[
        GetServiceVrfAssociatedRoutingOspfv3Ipv4FeaturesGetResponse
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospfv3.ipv4.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4/{ospfv3Id}
------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str, ospfv3_id: str
    ) -> GetSingleSdRoutingServiceVrfRoutingOspfv3Ipv4Payload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospfv3.ipv4.get()


.. toctree::
    :maxdepth: 1

    models

