=========================================================
v1.feature_profile.sd_routing.service.routing.ospfv3.ipv6
=========================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospfv3/ipv6
--------------------------------------------------------------------------------------------------


Create a SD-Routing LAN OSPFv3 IPv6 feature from a specific service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateSdroutingServiceVrfOspfv3Ipv6FeaturePostRequest,
    ) -> CreateSdroutingServiceVrfOspfv3Ipv6FeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.routing.ospfv3.ipv6.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospfv3/ipv6/{ospfv3Id}
------------------------------------------------------------------------------------------------------------


Edit the SD-Routing LAN OSPFv3 IPv6 feature from a specific service feature profile

.. code:: python

    def put(
        service_id: str,
        ospfv3_id: str,
        payload: EditSdroutingServiceVrfOspfv3Ipv6FeaturePutRequest,
    ) -> EditSdroutingServiceVrfOspfv3Ipv6FeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.routing.ospfv3.ipv6.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospfv3/ipv6/{ospfv3Id}
---------------------------------------------------------------------------------------------------------------


Delete the SD-Routing LAN OSPFv3 IPv6 feature from a specific service feature profile

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
        client.v1.feature_profile.sd_routing.service.routing.ospfv3.ipv6.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospfv3/ipv6
-------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
    ) -> GetListSdRoutingServiceRoutingOspfv3Ipv6Payload: ...


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
        client.v1.feature_profile.sd_routing.service.routing.ospfv3.ipv6.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/routing/ospfv3/ipv6/{ospfv3Id}
------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, ospfv3_id: str
    ) -> GetSingleSdRoutingServiceRoutingOspfv3Ipv6Payload: ...


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
        client.v1.feature_profile.sd_routing.service.routing.ospfv3.ipv6.get()


.. toctree::
    :maxdepth: 1

    models

