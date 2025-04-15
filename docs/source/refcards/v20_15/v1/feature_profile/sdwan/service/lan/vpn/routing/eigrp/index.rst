======================================================
v1.feature_profile.sdwan.service.lan.vpn.routing.eigrp
======================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp
-------------------------------------------------------------------------------------------------------


Associate a lanvpn feature with a routingeigrp Feature for service feature profile

.. code:: python

    def post(
        service_id: str,
        vpn_id: str,
        payload: CreateLanVpnAndRoutingEigrpParcelAssociationForServicePostRequest,
    ) -> (
        CreateLanVpnAndRoutingEigrpParcelAssociationForServicePostResponse
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.eigrp.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp/{eigrpId}
----------------------------------------------------------------------------------------------------------------


Update a LanVpn feature and a RoutingEigrp Feature association for service feature profile

.. code:: python

    def put(
        service_id: str,
        vpn_id: str,
        eigrp_id: str,
        payload: EditLanVpnAndRoutingEigrpParcelAssociationForServicePutRequest,
    ) -> (
        EditLanVpnAndRoutingEigrpParcelAssociationForServicePutResponse
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.eigrp.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp/{eigrpId}
-------------------------------------------------------------------------------------------------------------------


Delete a LanVpn feature and a RoutingEigrp Feature association for service feature profile

.. code:: python

    def delete(service_id: str, vpn_id: str, eigrp_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.eigrp.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp
------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str
    ) -> List[
        GetLanVpnAssociatedRoutingEigrpParcelsForServiceGetResponse
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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.eigrp.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/routing/eigrp/{eigrpId}
----------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str, eigrp_id: str
    ) -> GetSingleSdwanServiceLanVpnRoutingEigrpPayload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.routing.eigrp.get()


.. toctree::
    :maxdepth: 1

    models

