================================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.tracker
================================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker
---------------------------------------------------------------------------------------------------------------------------


Associate a WanVpnInterfaceGre parcel with a Tracker Parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vpn_id: str,
        gre_id: str,
        payload: CreateWanVpnInterfaceGreAndTrackerParcelAssociationForTransportPostRequest,
    ) -> CreateWanVpnInterfaceGreAndTrackerParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.tracker.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------------------------------------------------


Update a WanVpnInterfaceGre parcel and a Tracker Parcel association for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vpn_id: str,
        gre_id: str,
        tracker_id: str,
        payload: EditWanVpnInterfaceGreAndTrackerParcelAssociationForTransportPutRequest,
    ) -> EditWanVpnInterfaceGreAndTrackerParcelAssociationForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.tracker.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker/{trackerId}
-----------------------------------------------------------------------------------------------------------------------------------------


Delete a WanVpnInterfaceGre and a Tracker Parcel association for transport feature profile

.. code:: python

    def delete(
        transport_id: str, vpn_id: str, gre_id: str, tracker_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.tracker.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker
--------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, gre_id: str
    ) -> List[
        GetWanVpnInterfaceGreAssociatedTrackerParcelsForTransportGetResponse
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.tracker.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vpn_id: str, gre_id: str, tracker_id: str
    ) -> GetSingleSdwanTransportWanVpnInterfaceGreTrackerPayload: ...


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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.tracker.get()


.. toctree::
    :maxdepth: 1

    models

