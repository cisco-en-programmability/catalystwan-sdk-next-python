============================================================
v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv4
============================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv4
-------------------------------------------------------------------------------------------------------------


Associate a LAN VPN parcel with a IPv4 address family OSPFv3 Parcel for service feature profile

.. code:: python

    def post(
        service_id: str,
        vpn_id: str,
        payload: CreateLanVpnAndRoutingOspfv3IPv4ParcelAssociationForServicePostRequest,
    ) -> CreateLanVpnAndRoutingOspfv3IPv4ParcelAssociationForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv4.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv4/{ospfv3Id}
-----------------------------------------------------------------------------------------------------------------------


Update a LAN VPN parcel and a routing OSPFv3 IPv4 Parcel association for service feature profile

.. code:: python

    def put(
        service_id: str,
        vpn_id: str,
        ospfv3_id: str,
        payload: EditLanVpnAndRoutingOspfv3IPv4ParcelAssociationForServicePutRequest,
    ) -> EditLanVpnAndRoutingOspfv3IPv4ParcelAssociationForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv4.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv4/{ospfv3Id}
--------------------------------------------------------------------------------------------------------------------------


Delete a LAN VPN parcel and a IPv4 OSPFv3 parcel association for service feature profile

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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv4.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv4
------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str
    ) -> List[
        GetLanVpnAssociatedRoutingOspfv3IPv4ParcelsForServiceGetResponse
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv4.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospfv3/ipv4/{ospfv3Id}
-----------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str, ospfv3_id: str
    ) -> GetSingleSdwanServiceLanVpnRoutingOspfv3Ipv4Payload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospfv3.ipv4.get()


.. toctree::
    :maxdepth: 1

    models

