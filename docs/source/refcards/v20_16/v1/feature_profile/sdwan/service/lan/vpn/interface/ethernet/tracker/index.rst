===================================================================
v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.tracker
===================================================================


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------------------------------------------------------


Update a LanVpnInterfaceEthernet parcel and a Tracker Parcel association for service feature profile

.. code:: python

    def put(
        service_id: str,
        vpn_id: str,
        ethernet_id: str,
        tracker_id: str,
        payload: EditLanVpnInterfaceEthernetAndTrackerParcelAssociationForTransportPutRequest,
    ) -> EditLanVpnInterfaceEthernetAndTrackerParcelAssociationForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.tracker.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/tracker/{trackerId}
-----------------------------------------------------------------------------------------------------------------------------------------------


Delete a LanVpnInterfaceEthernet and a Tracker Parcel association for service feature profile

.. code:: python

    def delete(
        service_id: str, vpn_id: str, ethernet_id: str, tracker_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.tracker.delete()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnParcelId}/interface/ethernet/{ethernetId}/tracker
---------------------------------------------------------------------------------------------------------------------------------------


Associate a LanVpnInterfaceEthernet parcel with a Tracker Parcel for service feature profile

.. code:: python

    def post(
        service_id: str,
        vpn_parcel_id: str,
        ethernet_id: str,
        payload: CreateLanVpnInterfaceEthernetAndTrackerParcelAssociationForTransportPostRequest,
    ) -> CreateLanVpnInterfaceEthernetAndTrackerParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.tracker.post()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/tracker
--------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str, ethernet_id: str
    ) -> List[
        GetLanVpnInterfaceEthernetAssociatedTrackerParcelsForTransportGetResponse
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.tracker.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str, ethernet_id: str, tracker_id: str
    ) -> GetSingleSdwanServiceLanVpnInterfaceEthernetTrackerPayload: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.tracker.get()


.. toctree::
    :maxdepth: 1

    models

