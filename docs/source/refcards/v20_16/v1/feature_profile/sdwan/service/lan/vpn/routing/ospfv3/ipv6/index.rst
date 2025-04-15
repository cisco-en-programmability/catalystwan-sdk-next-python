============================================================
v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv6
============================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6
-------------------------------------------------------------------------------------------------------------


Associate a LAN VPN parcel with a IPv6 address family OSPFv3 Parcel for service feature profile

.. code:: python

    def post(
        service_id: str,
        vpn_id: str,
        payload: CreateLanVpnAndRoutingOspfv3IPv6ParcelAssociationForServicePostRequest,
    ) -> CreateLanVpnAndRoutingOspfv3IPv6ParcelAssociationForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv6.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6/{ospfv3Id}
-----------------------------------------------------------------------------------------------------------------------


Update a LAN VPN parcel and a routing OSPFv3 IPv6 Parcel association for service feature profile

.. code:: python

    def put(
        service_id: str,
        vpn_id: str,
        ospfv3_id: str,
        payload: EditLanVpnAndRoutingOspfv3IPv6ParcelAssociationForServicePutRequest,
    ) -> EditLanVpnAndRoutingOspfv3IPv6ParcelAssociationForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv6.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6/{ospfv3Id}
--------------------------------------------------------------------------------------------------------------------------


Delete a LAN VPN parcel and a IPv6 OSPFv3 parcel association for service feature profile

.. code:: python

    def delete(service_id: str, vpn_id: str, ospfv3_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv6.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6
------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str
    ) -> List[
        GetLanVpnAssociatedRoutingOspfv3IPv6ParcelsForServiceGetResponse
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv6.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv6/{ospfv3Id}
-----------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str, ospfv3_id: str
    ) -> GetSingleSdwanServiceLanVpnRoutingOspfv3Ipv6Payload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv6.get()


.. toctree::
    :maxdepth: 1

    models

