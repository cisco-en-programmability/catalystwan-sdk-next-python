=========================================================
v1.feature_profile.sd_routing.service.routing.ospfv3.ipv4
=========================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospfv3/ipv4
--------------------------------------------------------------------------------------------------


Create a SD-Routing LAN OSPFv3 IPv4 Feature for service VRF in Service Feature Profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateSdroutingServiceVrfOspfv3Ipv4FeaturePostRequest,
    ) -> CreateSdroutingServiceVrfOspfv3Ipv4FeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.routing.ospfv3.ipv4.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospfv3/ipv4/{ospfv3Id}
------------------------------------------------------------------------------------------------------------


Edit a SD-Routing LAN OSPFv3 IPv4 Feature for service VRF in Service Feature Profile

.. code:: python

    def put(
        service_id: str,
        ospfv3_id: str,
        payload: EditSdroutingServiceVrfOspfv3Ipv4FeaturePutRequest,
    ) -> EditSdroutingServiceVrfOspfv3Ipv4FeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.routing.ospfv3.ipv4.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospfv3/ipv4/{ospfv3Id}
---------------------------------------------------------------------------------------------------------------


Delete a SD-Routing LAN OSPFv3 IPv4 Feature for service VRF in Service Feature Profile

.. code:: python

    def delete(service_id: str, ospfv3_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.routing.ospfv3.ipv4.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospfv3/ipv4
-------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
    ) -> GetListSdRoutingServiceRoutingOspfv3Ipv4Payload: ...


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
        client.v1.feature_profile.sd_routing.service.routing.ospfv3.ipv4.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospfv3/ipv4/{ospfv3Id}
------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, ospfv3_id: str
    ) -> GetSingleSdRoutingServiceRoutingOspfv3Ipv4Payload: ...


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
        client.v1.feature_profile.sd_routing.service.routing.ospfv3.ipv4.get()


.. toctree::
    :maxdepth: 1

    models

