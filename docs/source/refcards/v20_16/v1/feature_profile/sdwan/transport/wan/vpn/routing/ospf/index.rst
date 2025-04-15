=======================================================
v1.feature_profile.sdwan.transport.wan.vpn.routing.ospf
=======================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf
----------------------------------------------------------------------------------------------------------


Associate a wan/vpn parcel with a routing/ospf Parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_id: str,
        payload: CreateWanVpnAndRoutingOspfParcelAssociationForTransportPostRequest,
    ) -> CreateWanVpnAndRoutingOspfParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospf.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf/{ospfId}
------------------------------------------------------------------------------------------------------------------


Update a WanVpn parcel and a RoutingOspf Parcel association for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        ospf_id: str,
        payload: EditWanVpnAndRoutingOspfParcelAssociationForTransportPutRequest,
    ) -> (
        EditWanVpnAndRoutingOspfParcelAssociationForTransportPutResponse
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospf.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf/{ospfId}
---------------------------------------------------------------------------------------------------------------------


Delete a WanVpn parcel and a RoutingOspf Parcel association for transport feature profile

.. code:: python

    def delete(transport_id: str, vpn_id: str, ospf_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospf.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf
---------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str
    ) -> List[
        GetWanVpnAssociatedRoutingOspfParcelsForTransportGetResponse
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospf.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/routing/ospf/{ospfId}
------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, ospf_id: str
    ) -> GetSingleSdwanTransportWanVpnRoutingOspfPayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.routing.ospf.get()


.. toctree::
    :maxdepth: 1

    models

