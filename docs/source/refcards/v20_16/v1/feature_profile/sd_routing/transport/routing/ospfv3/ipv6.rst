===========================================================
v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv6
===========================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospfv3/ipv6
-----------------------------------------------------------------------------------------------------


Get all SD-Routing WAN OSPFv3 IPv6 features from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_routing_ospfv3_ipv6_features(
        transport_id: str,
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv6.get_sdrouting_transport_routing_ospfv3_ipv6_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospfv3/ipv6
------------------------------------------------------------------------------------------------------


Create a SD-Routing WAN OSPFv3 IPv6 feature from a specific transport feature profile

.. code:: python

    def create_sdrouting_transport_routing_ospfv3_ipv6_feature(
        transport_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv6.create_sdrouting_transport_routing_ospfv3_ipv6_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospfv3/ipv6/{ospfv3Id}
----------------------------------------------------------------------------------------------------------------


Get the SD-Routing WAN OSPFv3 IPv6 feature from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_routing_ospfv3_ipv6_feature(
        transport_id: str, ospfv3_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv6.get_sdrouting_transport_routing_ospfv3_ipv6_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospfv3/ipv6/{ospfv3Id}
----------------------------------------------------------------------------------------------------------------


Edit the SD-Routing WAN OSPFv3 IPv6 feature from a specific transport feature profile

.. code:: python

    def edit_sdrouting_transport_routing_ospfv3_ipv6_feature(
        transport_id: str, ospfv3_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv6.edit_sdrouting_transport_routing_ospfv3_ipv6_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospfv3/ipv6/{ospfv3Id}
-------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing WAN OSPFv3 IPv6 feature from a specific transport feature profile

.. code:: python

    def delete_sdrouting_transport_routing_ospfv3_ipv6_feature(
        transport_id: str, ospfv3_id: str
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
        client.v1.feature_profile.sd_routing.transport.routing.ospfv3.ipv6.delete_sdrouting_transport_routing_ospfv3_ipv6_feature()


