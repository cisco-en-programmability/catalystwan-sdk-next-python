==================================================
v1.feature_profile.sd_routing.service.routing.ospf
==================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf
-------------------------------------------------------------------------------------------


Create a SD-Routing LAN OSPF Feature for service VRF in Service Feature Profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateSdroutingServiceVrfOspfFeaturePostRequest,
    ) -> CreateSdroutingServiceVrfOspfFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.routing.ospf.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf/{ospfId}
---------------------------------------------------------------------------------------------------


Edit a SD-Routing LAN OSPF Feature for service VRF in Service Feature Profile

.. code:: python

    def put(
        service_id: str,
        ospf_id: str,
        payload: EditSdroutingServiceVrfOspfFeaturePutRequest,
    ) -> EditSdroutingServiceVrfOspfFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.routing.ospf.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf/{ospfId}
------------------------------------------------------------------------------------------------------


Delete a SD-Routing LAN OSPF Feature for service VRF in Service Feature Profile

.. code:: python

    def delete(service_id: str, ospf_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.routing.ospf.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf
------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
    ) -> GetListSdRoutingServiceRoutingOspfPayload: ...


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
        client.v1.feature_profile.sd_routing.service.routing.ospf.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospf/{ospfId}
---------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, ospf_id: str
    ) -> GetSingleSdRoutingServiceRoutingOspfPayload: ...


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
        client.v1.feature_profile.sd_routing.service.routing.ospf.get()


.. toctree::
    :maxdepth: 1

    models

