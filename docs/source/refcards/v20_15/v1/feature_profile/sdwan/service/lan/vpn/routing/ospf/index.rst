=====================================================
v1.feature_profile.sdwan.service.lan.vpn.routing.ospf
=====================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospf
------------------------------------------------------------------------------------------------------


Associate a lanvpn parcel with a routingospf Parcel for service feature profile

.. code:: python

    def post(
        service_id: str,
        vpn_id: str,
        payload: CreateLanVpnAndRoutingOspfParcelAssociationForServicePostRequest,
    ) -> (
        CreateLanVpnAndRoutingOspfParcelAssociationForServicePostResponse
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospf.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospf/{ospfId}
--------------------------------------------------------------------------------------------------------------


Update a LanVpn parcel and a RoutingOspf Parcel association for service feature profile

.. code:: python

    def put(
        service_id: str,
        vpn_id: str,
        ospf_id: str,
        payload: EditLanVpnAndRoutingOspfParcelAssociationForServicePutRequest,
    ) -> (
        EditLanVpnAndRoutingOspfParcelAssociationForServicePutResponse
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospf.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospf/{ospfId}
-----------------------------------------------------------------------------------------------------------------


Delete a LanVpn parcel and a RoutingOspf Parcel association for service feature profile

.. code:: python

    def delete(service_id: str, vpn_id: str, ospf_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospf.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospf
-----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str
    ) -> List[
        GetLanVpnAssociatedRoutingOspfParcelsForServiceGetResponse
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospf.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/ospf/{ospfId}
--------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str, ospf_id: str
    ) -> GetSingleSdwanServiceLanVpnRoutingOspfPayload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.ospf.get()


.. toctree::
    :maxdepth: 1

    models

