=====================================================
v1.feature_profile.sd_routing.service.vrf.routing.bgp
=====================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp
---------------------------------------------------------------------------------------------


Get all SD-Routing LAN BGP features from a specific service feature profile

.. code:: python

    def get_sdrouting_service_vrf_bgp_features(
        service_id: str,
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.get_sdrouting_service_vrf_bgp_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp
----------------------------------------------------------------------------------------------


Create a SD-Routing LAN BGP feature from a specific service feature profile

.. code:: python

    def create_sdrouting_service_vrf_bgp_feature(
        service_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.create_sdrouting_service_vrf_bgp_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp/{bgpId}
-----------------------------------------------------------------------------------------------------


Get the SD-Routing LAN BGP feature from a specific service feature profile

.. code:: python

    def get_sdrouting_service_vrf_bgp_feature(
        service_id: str, bgp_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.get_sdrouting_service_vrf_bgp_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp/{bgpId}
-----------------------------------------------------------------------------------------------------


Edit the SD-Routing LAN BGP feature from a specific service feature profile

.. code:: python

    def edit_sdrouting_service_vrf_bgp_feature(
        service_id: str, bgp_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.edit_sdrouting_service_vrf_bgp_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/routing/bgp/{bgpId}
--------------------------------------------------------------------------------------------------------


Delete the SD-Routing LAN BGP feature from a specific service feature profile

.. code:: python

    def delete_sdrouting_service_vrf_bgp_feature(
        service_id: str, bgp_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.delete_sdrouting_service_vrf_bgp_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/bgp
-----------------------------------------------------------------------------------------------------


Get the LAN VRF associated BGP Features for service feature profile

.. code:: python

    def get_service_vrf_associated_routing_bgp_features(
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.get_service_vrf_associated_routing_bgp_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/bgp
------------------------------------------------------------------------------------------------------


Associate a BGP feature with the LAN VRF feature for service feature profile

.. code:: python

    def create_service_vrf_and_routing_bgp_feature_association(
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.create_service_vrf_and_routing_bgp_feature_association()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/bgp/{bgpId}
-------------------------------------------------------------------------------------------------------------


Get VRF parcel associated RoutingBGP Parcel by bgpId for service feature profile

.. code:: python

    def get_service_vrf_associated_routing_bgp_parcel_by_parcel_id(
        service_id: str, vrf_id: str, bgp_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.get_service_vrf_associated_routing_bgp_parcel_by_parcel_id()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/bgp/{bgpId}
-------------------------------------------------------------------------------------------------------------


Replace the BGP feature for LAN VRF feature in service feature profile

.. code:: python

    def edit_service_vrf_and_routing_bgp_feature_association(
        service_id: str,
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.edit_service_vrf_and_routing_bgp_feature_association()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/routing/bgp/{bgpId}
----------------------------------------------------------------------------------------------------------------


Delete the LAN VRF feature and BGP feature association for service feature profile

.. code:: python

    def delete_service_vrf_and_routing_bgp_association(
        service_id: str, vrf_id: str, bgp_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.routing.bgp.delete_service_vrf_and_routing_bgp_association()


