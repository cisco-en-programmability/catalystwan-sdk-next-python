======================================================
v1.feature_profile.sd_routing.service.vrf.dmvpn_tunnel
======================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel
------------------------------------------------------------------------------------------------------


Get all SD-Routing VRF DMVPN Tunnel features from a specific service feature profile

.. code:: python

    def get_sdrouting_service_vrf_dmvpn_tunnel_features(
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
        client.v1.feature_profile.sd_routing.service.vrf.dmvpn_tunnel.get_sdrouting_service_vrf_dmvpn_tunnel_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel
-------------------------------------------------------------------------------------------------------


Create a SD-Routing VRF DMVPN Tunnel feature from a specific service feature profile

.. code:: python

    def create_sdrouting_service_vrf_dmvpn_tunnel_feature(
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
        client.v1.feature_profile.sd_routing.service.vrf.dmvpn_tunnel.create_sdrouting_service_vrf_dmvpn_tunnel_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel/{tunnelId}
-----------------------------------------------------------------------------------------------------------------


Get the SD-Routing VRF DMVPN Tunnel feature from a specific service feature profile

.. code:: python

    def get_sdrouting_service_vrf_dmvpn_tunnel_feature(
        service_id: str, vrf_id: str, tunnel_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.dmvpn_tunnel.get_sdrouting_service_vrf_dmvpn_tunnel_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel/{tunnelId}
-----------------------------------------------------------------------------------------------------------------


Edit the SD-Routing VRF DMVPN Tunnel feature from a specific service feature profile

.. code:: python

    def edit_sdrouting_service_vrf_dmvpn_tunnel_feature(
        service_id: str,
        vrf_id: str,
        tunnel_id: str,
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
        client.v1.feature_profile.sd_routing.service.vrf.dmvpn_tunnel.edit_sdrouting_service_vrf_dmvpn_tunnel_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel/{tunnelId}
--------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing VRF DMVPN Tunnel feature from a specific service feature profile

.. code:: python

    def delete_sdrouting_service_vrf_dmvpn_tunnel_feature(
        service_id: str, vrf_id: str, tunnel_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.dmvpn_tunnel.delete_sdrouting_service_vrf_dmvpn_tunnel_feature()


