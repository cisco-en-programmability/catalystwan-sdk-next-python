======================================================
v1.feature_profile.sd_routing.service.vrf.dmvpn_tunnel
======================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/dmvpn-tunnel
-------------------------------------------------------------------------------------------------------


Create a SD-Routing VRF DMVPN Tunnel Feature for Service Feature Profile

.. code:: python

    def post(
        service_id: str,
        vrf_id: str,
        payload: CreateSdroutingServiceVrfDmvpnTunnelFeatureForServicePostRequest,
    ) -> (
        CreateSdroutingServiceVrfDmvpnTunnelFeatureForServicePostResponse
    ): ...


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


Edit a SD-Routing VRF DMVPN Tunnel Feature for Service Feature Profile

.. code:: python

    def put(
        service_id: str,
        vrf_id: str,
        tunnel_id: str,
        payload: EditSdroutingServiceVrfDmvpnTunnelFeatureForServicePutRequest,
    ) -> (
        EditSdroutingServiceVrfDmvpnTunnelFeatureForServicePutResponse
    ): ...


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


Delete a SD-Routing VRF DMVPN Tunnel Feature for Service Feature Profile

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

