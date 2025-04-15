======================================================
v1.feature_profile.sd_routing.service.vrf.dmvpn_tunnel
======================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel
-------------------------------------------------------------------------------------------------------


Create a SD-Routing VRF DMVPN Tunnel feature from a specific service feature profile

.. code:: python

    def post(
        service_id: str,
        vrf_id: str,
        payload: CreateSdroutingServiceVrfDmvpnTunnelFeaturePostRequest,
    ) -> CreateSdroutingServiceVrfDmvpnTunnelFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.dmvpn_tunnel.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel/{tunnelId}
-----------------------------------------------------------------------------------------------------------------


Edit the SD-Routing VRF DMVPN Tunnel feature from a specific service feature profile

.. code:: python

    def put(
        service_id: str,
        vrf_id: str,
        tunnel_id: str,
        payload: EditSdroutingServiceVrfDmvpnTunnelFeaturePutRequest,
    ) -> EditSdroutingServiceVrfDmvpnTunnelFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.dmvpn_tunnel.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel/{tunnelId}
--------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing VRF DMVPN Tunnel feature from a specific service feature profile

.. code:: python

    def delete(service_id: str, vrf_id: str, tunnel_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.dmvpn_tunnel.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel
------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str
    ) -> GetListSdRoutingServiceVrfLanDmvpnTunnelPayload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.dmvpn_tunnel.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel/{tunnelId}
-----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str, tunnel_id: str
    ) -> GetSingleSdRoutingServiceVrfLanDmvpnTunnelPayload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.dmvpn_tunnel.get()


.. toctree::
    :maxdepth: 1

    models

