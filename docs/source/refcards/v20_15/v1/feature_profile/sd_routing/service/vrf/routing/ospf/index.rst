======================================================
v1.feature_profile.sd_routing.service.vrf.routing.ospf
======================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf
-------------------------------------------------------------------------------------------------------


Associate an OSPF feature with the LAN VRF feature for service feature profile

.. code:: python

    def post(
        service_id: str,
        vrf_id: str,
        payload: CreateServiceVrfAndRoutingOspfParcelAssociationPostRequest,
    ) -> CreateServiceVrfAndRoutingOspfParcelAssociationPostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospf.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf/{ospfId}
---------------------------------------------------------------------------------------------------------------


Replace the OSPF feature for LAN VRF feature in service feature profile

.. code:: python

    def put(
        service_id: str,
        vrf_id: str,
        ospf_id: str,
        payload: EditServiceVrfAndRoutingOspfFeatureAssociationPutRequest,
    ) -> EditServiceVrfAndRoutingOspfFeatureAssociationPutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospf.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf/{ospfId}
------------------------------------------------------------------------------------------------------------------


Delete the LAN VRF feature and OSPF feature association in service feature profile

.. code:: python

    def delete(service_id: str, vrf_id: str, ospf_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospf.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf
------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str
    ) -> List[GetServiceVrfAssociatedRoutingOspfFeaturesGetResponse]: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospf.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospf/{ospfId}
---------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str, ospf_id: str
    ) -> GetSingleSdRoutingServiceVrfRoutingOspfPayload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospf.get()


.. toctree::
    :maxdepth: 1

    models

