====================================================
v1.feature_profile.sdwan.service.lan.vpn.routing.bgp
====================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp
-----------------------------------------------------------------------------------------------------


Associate a lanvpn parcel with a routingbgp Parcel for service feature profile

.. code:: python

    def post(
        service_id: str,
        vpn_id: str,
        payload: CreateLanVpnAndRoutingBgpParcelAssociationForServicePostRequest,
    ) -> (
        CreateLanVpnAndRoutingBgpParcelAssociationForServicePostResponse
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.bgp.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp/{bgpId}
------------------------------------------------------------------------------------------------------------


Update a LanVpn parcel and a RoutingBgp Parcel association for service feature profile

.. code:: python

    def put(
        service_id: str,
        vpn_id: str,
        bgp_id: str,
        payload: EditLanVpnAndRoutingBgpParcelAssociationForServicePutRequest,
    ) -> (
        EditLanVpnAndRoutingBgpParcelAssociationForServicePutResponse
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.bgp.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp/{bgpId}
---------------------------------------------------------------------------------------------------------------


Delete a LanVpn parcel and a RoutingBgp Parcel association for service feature profile

.. code:: python

    def delete(service_id: str, vpn_id: str, bgp_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.bgp.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp
----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str
    ) -> List[
        GetLanVpnAssociatedRoutingBgpParcelsForServiceGetResponse
    ]: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.bgp.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/bgp/{bgpId}
------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str, bgp_id: str
    ) -> GetSingleSdwanServiceLanVpnRoutingBgpPayload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.bgp.get()


.. toctree::
    :maxdepth: 1

    models

