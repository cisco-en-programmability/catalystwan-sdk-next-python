===========================================================
v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv6
===========================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospfv3/ipv6
------------------------------------------------------------------------------------------------------


Create a SD-Routing WAN OSPFv3 IPv6 feature from a specific transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateSdroutingTransportRoutingOspfv3Ipv6FeaturePostRequest,
    ) -> CreateSdroutingTransportRoutingOspfv3Ipv6FeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv6.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospfv3/ipv6/{ospfv3Id}
----------------------------------------------------------------------------------------------------------------


Edit the SD-Routing WAN OSPFv3 IPv6 feature from a specific transport feature profile

.. code:: python

    def put(
        transport_id: str,
        ospfv3_id: str,
        payload: EditSdroutingTransportRoutingOspfv3Ipv6FeaturePutRequest,
    ) -> EditSdroutingTransportRoutingOspfv3Ipv6FeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv6.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospfv3/ipv6/{ospfv3Id}
-------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing WAN OSPFv3 IPv6 feature from a specific transport feature profile

.. code:: python

    def delete(transport_id: str, ospfv3_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv6.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospfv3/ipv6
-----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdRoutingTransportRoutingOspfv3Ipv6Payload: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv6.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospfv3/ipv6/{ospfv3Id}
----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, ospfv3_id: str
    ) -> GetSingleSdRoutingTransportRoutingOspfv3Ipv6Payload: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv6.get()


.. toctree::
    :maxdepth: 1

    models

