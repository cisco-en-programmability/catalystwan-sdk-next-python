========================================================================
v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.trackergroup
========================================================================


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup/{trackergroupId}
------------------------------------------------------------------------------------------------------------------------------------------------------


Update a LanVpnInterfaceEthernet parcel and a TrackerGroup Parcel association for service feature profile

.. code:: python

    def put(
        service_id: str,
        vpn_id: str,
        ethernet_id: str,
        trackergroup_id: str,
        payload: EditLanVpnInterfaceEthernetAndTrackerGroupParcelAssociationForTransportPutRequest,
    ) -> EditLanVpnInterfaceEthernetAndTrackerGroupParcelAssociationForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.trackergroup.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup/{trackergroupId}
---------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a LanVpnInterfaceEthernet and a TrackerGroup Parcel association for service feature profile

.. code:: python

    def delete(
        service_id: str,
        vpn_id: str,
        ethernet_id: str,
        trackergroup_id: str,
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.trackergroup.delete()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnParcelId}/interface/ethernet/{ethernetId}/trackergroup
--------------------------------------------------------------------------------------------------------------------------------------------


Associate a LanVpnInterfaceEthernet parcel with a TrackerGroup Parcel for service feature profile

.. code:: python

    def post(
        service_id: str,
        vpn_parcel_id: str,
        ethernet_id: str,
        payload: CreateLanVpnInterfaceEthernetAndTrackerGroupParcelAssociationForTransportPostRequest,
    ) -> CreateLanVpnInterfaceEthernetAndTrackerGroupParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.trackergroup.post()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup
-------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vpn_id: str, ethernet_id: str
    ) -> List[
        GetLanVpnInterfaceEthernetAssociatedTrackerGroupParcelsForTransportGetResponse
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.trackergroup.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup/{trackergroupId}
------------------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
        vpn_id: str,
        ethernet_id: str,
        trackergroup_id: str,
    ) -> (
        GetSingleSdwanServiceLanVpnInterfaceEthernetTrackergroupPayload
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.trackergroup.get()


.. toctree::
    :maxdepth: 1

    models

