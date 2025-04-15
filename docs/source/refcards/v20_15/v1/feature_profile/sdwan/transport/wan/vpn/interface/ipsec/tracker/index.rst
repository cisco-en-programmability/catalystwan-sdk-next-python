==================================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.tracker
==================================================================


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec/{ipsecId}/tracker/{trackerId}
------------------------------------------------------------------------------------------------------------------------------------------


Update a WanVpnInterfaceIpsec parcel and a Tracker Parcel association for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        ipsec_id: str,
        tracker_id: str,
        payload: EditWanVpnInterfaceIpsecAndTrackerParcelAssociationForTransportPutRequest,
    ) -> EditWanVpnInterfaceIpsecAndTrackerParcelAssociationForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.tracker.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec/{ipsecId}/tracker/{trackerId}
---------------------------------------------------------------------------------------------------------------------------------------------


Delete a WanVpnInterfaceIpsec and a Tracker Parcel association for transport feature profile

.. code:: python

    def delete(
        transport_id: str, vpn_id: str, ipsec_id: str, tracker_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.tracker.delete()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnParcelId}/interface/ipsec/{ipsecId}/tracker
-------------------------------------------------------------------------------------------------------------------------------------


Associate a WanVpnInterfaceIpsec parcel with a Tracker Parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_parcel_id: str,
        ipsec_id: str,
        payload: CreateWanVpnInterfaceIpsecAndTrackerParcelAssociationForTransportPostRequest,
    ) -> CreateWanVpnInterfaceIpsecAndTrackerParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.tracker.post()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec/{ipsecId}/tracker
------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, ipsec_id: str
    ) -> List[
        GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransportGetResponse
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.tracker.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec/{ipsecId}/tracker/{trackerId}
------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, ipsec_id: str, tracker_id: str
    ) -> GetSingleSdwanTransportWanVpnInterfaceIpsecTrackerPayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.tracker.get()


.. toctree::
    :maxdepth: 1

    models

