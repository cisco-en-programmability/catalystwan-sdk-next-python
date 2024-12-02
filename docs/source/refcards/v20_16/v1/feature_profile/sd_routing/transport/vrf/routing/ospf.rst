========================================================
v1.feature_profile.sd_routing.transport.vrf.routing.ospf
========================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospf
----------------------------------------------------------------------------------------------------------


Get the WAN VRF associated OSPF features for transport feature profile

.. code:: python

    def get_transport_vrf_associated_routing_ospf_features_1(
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.ospf.get_transport_vrf_associated_routing_ospf_features_1()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospf
-----------------------------------------------------------------------------------------------------------


Associate an OSPF feature with the WAN VRF feature for transport feature profile

.. code:: python

    def create_transport_vrf_and_routing_ospf_association(
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.ospf.create_transport_vrf_and_routing_ospf_association()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospf/{ospfId}
-------------------------------------------------------------------------------------------------------------------


Get the WAN VRF associated OSPF features by feature ID for transport feature profile

.. code:: python

    def get_vrf_associated_routing_ospf_by_id(
        transport_id: str, vrf_id: str, ospf_id: str
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.ospf.get_vrf_associated_routing_ospf_by_id()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospf/{ospfId}
-------------------------------------------------------------------------------------------------------------------


Replace the OSPF feature for the WAN VRF feature in transport feature profile

.. code:: python

    def edit_transport_vrf_and_routing_ospf_feature_association(
        transport_id: str,
        vrf_id: str,
        ospf_id: str,
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.ospf.edit_transport_vrf_and_routing_ospf_feature_association()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/ospf/{ospfId}
----------------------------------------------------------------------------------------------------------------------


Delete the VRF and OSPF feature association for transport feature profile

.. code:: python

    def delete_transport_vrf_and_routing_ospf_association(
        transport_id: str, vrf_id: str, ospf_id: str
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.ospf.delete_transport_vrf_and_routing_ospf_association()


