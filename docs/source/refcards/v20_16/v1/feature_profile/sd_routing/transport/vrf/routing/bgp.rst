=======================================================
v1.feature_profile.sd_routing.transport.vrf.routing.bgp
=======================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/routing/bgp
-------------------------------------------------------------------------------------------------


Get all SD-Routing WAN BGP features for VRF from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_vrf_bgp_features(
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.get_sdrouting_transport_vrf_bgp_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/routing/bgp
--------------------------------------------------------------------------------------------------


Create a SD-Routing WAN BGP feature for VRF from a specific transport feature profile

.. code:: python

    def create_sdrouting_transport_vrf_bgp_feature(
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.create_sdrouting_transport_vrf_bgp_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/routing/bgp/{bgpId}
---------------------------------------------------------------------------------------------------------


Get the SD-Routing WAN BGP feature for VRF from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_vrf_bgp_feature(
        transport_id: str, bgp_id: str
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.get_sdrouting_transport_vrf_bgp_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/routing/bgp/{bgpId}
---------------------------------------------------------------------------------------------------------


Edit the SD-Routing WAN BGP feature for VRF from a specific transport feature profile

.. code:: python

    def edit_sdrouting_transport_vrf_bgp_feature(
        transport_id: str, bgp_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.edit_sdrouting_transport_vrf_bgp_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/routing/bgp/{bgpId}
------------------------------------------------------------------------------------------------------------


Delete the SD-Routing WAN BGP feature for VRF from a specific transport feature profile

.. code:: python

    def delete_sdrouting_transport_vrf_bgp_feature(
        transport_id: str, bgp_id: str
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.delete_sdrouting_transport_vrf_bgp_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/bgp
---------------------------------------------------------------------------------------------------------


Get the WAN VRF associated BGP features for transport feature profile

.. code:: python

    def get_transport_vrf_associated_routing_bgp_features_1(
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.get_transport_vrf_associated_routing_bgp_features_1()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/bgp
----------------------------------------------------------------------------------------------------------


Associate a BGP feature with the WAN VRF feature for transport feature profile

.. code:: python

    def create_transport_vrf_and_routing_bgp_feature_association(
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.create_transport_vrf_and_routing_bgp_feature_association()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/bgp/{bgpId}
-----------------------------------------------------------------------------------------------------------------


Get the WAN VRF associated BGP feature by BGP feature ID for transport feature profile

.. code:: python

    def get_transport_vrf_associated_routing_bgp_by_id(
        transport_id: str, vrf_id: str, bgp_id: str
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.get_transport_vrf_associated_routing_bgp_by_id()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/bgp/{bgpId}
-----------------------------------------------------------------------------------------------------------------


Replace the BGP feature for the WAN VRF feature in transport feature profile

.. code:: python

    def edit_transport_vrf_and_routing_bgp_feature_association(
        transport_id: str,
        vrf_id: str,
        bgp_id: str,
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.edit_transport_vrf_and_routing_bgp_feature_association()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/routing/bgp/{bgpId}
--------------------------------------------------------------------------------------------------------------------


Delete the WAN VRF and BGP association for transport feature profile

.. code:: python

    def delete_transport_vrf_and_routing_bgp_association(
        transport_id: str, vrf_id: str, bgp_id: str
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
        client.v1.feature_profile.sd_routing.transport.vrf.routing.bgp.delete_transport_vrf_and_routing_bgp_association()


