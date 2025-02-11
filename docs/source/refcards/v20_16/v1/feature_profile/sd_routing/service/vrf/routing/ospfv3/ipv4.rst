=============================================================
v1.feature_profile.sd_routing.service.vrf.routing.ospfv3.ipv4
=============================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4
-------------------------------------------------------------------------------------------------------------


Get LAN VRF associated OSPFv3 IPv4 features for service feature profile

.. code:: python

    def get_service_vrf_associated_routing_ospfv3_ipv4_features(
        service_id: str, vrf_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospfv3.ipv4.get_service_vrf_associated_routing_ospfv3_ipv4_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4
--------------------------------------------------------------------------------------------------------------


Associate an OSPFv3 IPv4 feature with the LAN VRF feature for service feature profile

.. code:: python

    def create_service_vrf_and_routing_ospfv3_ipv4_feature_association(
        service_id: str, vrf_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospfv3.ipv4.create_service_vrf_and_routing_ospfv3_ipv4_feature_association()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4/{ospfv3Id}
------------------------------------------------------------------------------------------------------------------------


Get the VRF feature associated OSPFv3 IPv4 feature by ID for service feature profile

.. code:: python

    def get_service_vrf_associated_routing_ospfv3_ipv4_feature_by_id(
        service_id: str, vrf_id: str, ospfv3_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospfv3.ipv4.get_service_vrf_associated_routing_ospfv3_ipv4_feature_by_id()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4/{ospfv3Id}
------------------------------------------------------------------------------------------------------------------------


Replace the OSPFv3 IPv4 feature for LAN VRF feature in service feature profile

.. code:: python

    def edit_service_vrf_and_routing_ospfv3_ipv4_feature_association(
        service_id: str,
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospfv3.ipv4.edit_service_vrf_and_routing_ospfv3_ipv4_feature_association()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/ospfv3/ipv4/{ospfv3Id}
---------------------------------------------------------------------------------------------------------------------------


Delete the VRF feature and OSPFv3 IPv4 feature association for service feature profile

.. code:: python

    def delete_service_vrf_and_routing_ospfv3_ipv4_association(
        service_id: str, vrf_id: str, ospfv3_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.ospfv3.ipv4.delete_service_vrf_and_routing_ospfv3_ipv4_association()


