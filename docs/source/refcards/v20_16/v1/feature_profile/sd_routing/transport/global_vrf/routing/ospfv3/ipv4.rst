======================================================================
v1.feature_profile.sd_routing.transport.global_vrf.routing.ospfv3.ipv4
======================================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv4
------------------------------------------------------------------------------------------------------------------------


Get the Global VRF associated OSPFv3 IPv4 features for transport feature profile

.. code:: python

    def get_transport_vrf_associated_routing_ospfv3_ipv4_features(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.ospfv3.ipv4.get_transport_vrf_associated_routing_ospfv3_ipv4_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv4
-------------------------------------------------------------------------------------------------------------------------


Associate an OSPFv3 IPv4 feature with the global VRF feature for transport feature profile

.. code:: python

    def create_transport_global_vrf_and_routing_ospfv3_ipv4_feature_association(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.ospfv3.ipv4.create_transport_global_vrf_and_routing_ospfv3_ipv4_feature_association()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv4/{ospfv3Id}
-----------------------------------------------------------------------------------------------------------------------------------


Get the global VRF feature associated OSPFv3 IPv4 feature by ID for transport feature profile

.. code:: python

    def get_vrf_associated_routing_ospfv3_ipv4_feature_by_id(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.ospfv3.ipv4.get_vrf_associated_routing_ospfv3_ipv4_feature_by_id()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv4/{ospfv3Id}
-----------------------------------------------------------------------------------------------------------------------------------


Replace the OSPFv3 IPv4 feature for the global VRF feature in transport feature profile

.. code:: python

    def edit_transport_global_vrf_and_routing_ospfv3_ipv4_feature_association(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.ospfv3.ipv4.edit_transport_global_vrf_and_routing_ospfv3_ipv4_feature_association()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/routing/ospfv3/ipv4/{ospfv3Id}
--------------------------------------------------------------------------------------------------------------------------------------


Delete the global VRF and the OSPFv3 IPv4 feature association for transport feature profile

.. code:: python

    def delete_transport_global_vrf_and_routing_ospfv3_ipv4_association(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.routing.ospfv3.ipv4.delete_transport_global_vrf_and_routing_ospfv3_ipv4_association()


