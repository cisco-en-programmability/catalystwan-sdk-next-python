===========================================================
v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv4
===========================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospfv3/ipv4
------------------------------------------------------------------------------------------------------


Create a SD-Routing WAN OSPFv3 IPv4 Feature in Transport Feature Profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateSdroutingTransportRoutingOspfv3Ipv4FeaturePostRequest,
    ) -> CreateSdroutingTransportRoutingOspfv3Ipv4FeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv4.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospfv3/ipv4/{ospfv3Id}
----------------------------------------------------------------------------------------------------------------


Edit a SD-Routing WAN OSPFv3 IPv4 Feature in Transport Feature Profile

.. code:: python

    def put(
        transport_id: str,
        ospfv3_id: str,
        payload: EditSdroutingTransportRoutingOspfv3Ipv4FeaturePutRequest,
    ) -> EditSdroutingTransportRoutingOspfv3Ipv4FeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv4.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospfv3/ipv4/{ospfv3Id}
-------------------------------------------------------------------------------------------------------------------


Delete a SD-Routing WAN OSPFv3 IPv4 Feature in Transport Feature Profile

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
        client.v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv4.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospfv3/ipv4
-----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdRoutingTransportRoutingOspfv3Ipv4Payload: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv4.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospfv3/ipv4/{ospfv3Id}
----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, ospfv3_id: str
    ) -> GetSingleSdRoutingTransportRoutingOspfv3Ipv4Payload: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv4.get()


.. toctree::
    :maxdepth: 1

    models

