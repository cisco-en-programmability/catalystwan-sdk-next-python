==========================================================
v1.feature_profile.sdwan.service.lan.vpn.routing.multicast
==========================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast
-----------------------------------------------------------------------------------------------------------


Associate a lanvpn parcel with a routingmulticast Parcel for service feature profile

.. code:: python

    def post(
        service_id: str,
        vpn_id: str,
        payload: CreateLanVpnAndRoutingMulticastParcelAssociationForServicePostRequest,
    ) -> CreateLanVpnAndRoutingMulticastParcelAssociationForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.multicast.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast/{multicastId}
------------------------------------------------------------------------------------------------------------------------


Update a LanVpn parcel and a RoutingMulticast Parcel association for service feature profile

.. code:: python

    def put(
        service_id: str,
        vpn_id: str,
        multicast_id: str,
        payload: EditLanVpnAndRoutingMulticastParcelAssociationForServicePutRequest,
    ) -> EditLanVpnAndRoutingMulticastParcelAssociationForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.multicast.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast/{multicastId}
---------------------------------------------------------------------------------------------------------------------------


Delete a LanVpn parcel and a RoutingMulticast Parcel association for service feature profile

.. code:: python

    def delete(
        service_id: str, vpn_id: str, multicast_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.multicast.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast
----------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str
    ) -> List[
        GetLanVpnAssociatedRoutingMulticastParcelsForServiceGetResponse
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.multicast.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/multicast/{multicastId}
------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str, multicast_id: str
    ) -> GetSingleSdwanServiceLanVpnRoutingMulticastPayload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.multicast.get()


.. toctree::
    :maxdepth: 1

    models

