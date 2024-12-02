===============================================================
v1.feature_profile.sd_routing.transport.vrf.routing.ospfv3.ipv6
===============================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospfv3/ipv6
-----------------------------------------------------------------------------------------------------------------


Get the WAN VRF associated OSPFv3 IPv6 features for transport feature profile

.. code:: python

    def get_transport_vrf_associated_routing_ospfv3_ipv6_features_1(
        transport_id: str, vrf_id: str
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.ospfv3.ipv6.get_transport_vrf_associated_routing_ospfv3_ipv6_features_1()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospfv3/ipv6
------------------------------------------------------------------------------------------------------------------


Associate an OSPFv3 IPv6 feature with the WAN VRF feature for transport feature profile

.. code:: python

    def create_transport_vrf_and_routing_ospfv3_ipv6_feature_association(
        transport_id: str, vrf_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.ospfv3.ipv6.create_transport_vrf_and_routing_ospfv3_ipv6_feature_association()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospfv3/ipv6/{ospfv3Id}
----------------------------------------------------------------------------------------------------------------------------


Get the WAN VRF feature associated OSPFv3 IPv6 feature by ID for transport feature profile

.. code:: python

    def get_vrf_associated_routing_ospfv3_ipv6_feature_by_id_1(
        transport_id: str, vrf_id: str, ospfv3_id: str
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.ospfv3.ipv6.get_vrf_associated_routing_ospfv3_ipv6_feature_by_id_1()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospfv3/ipv6/{ospfv3Id}
----------------------------------------------------------------------------------------------------------------------------


Replace the OSPFv3 IPv6 feature for the WAN VRF feature in transport feature profile

.. code:: python

    def edit_transport_vrf_and_routing_ospfv3_ipv6_feature_association(
        transport_id: str,
        vrf_id: str,
        ospfv3_id: str,
        payload: Optional[str] = None,
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.ospfv3.ipv6.edit_transport_vrf_and_routing_ospfv3_ipv6_feature_association()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospfv3/ipv6/{ospfv3Id}
-------------------------------------------------------------------------------------------------------------------------------


Delete the WAN VRF feature and OSPFv3 IPv6 feature association for transport feature profile

.. code:: python

    def delete_transport_vrf_and_routing_ospfv3_ipv6_association(
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.ospfv3.ipv6.delete_transport_vrf_and_routing_ospfv3_ipv6_association()


