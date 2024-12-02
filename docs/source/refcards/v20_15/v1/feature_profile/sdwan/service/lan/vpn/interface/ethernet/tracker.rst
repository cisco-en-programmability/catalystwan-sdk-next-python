===================================================================
v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.tracker
===================================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/tracker
--------------------------------------------------------------------------------------------------------------------------------


Get LanVpnInterfaceEthernet associated Tracker Parcels for service feature profile

.. code:: python

    def get_lan_vpn_interface_ethernet_associated_tracker_parcels_for_transport(
        service_id: str, vpn_id: str, ethernet_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.tracker.get_lan_vpn_interface_ethernet_associated_tracker_parcels_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------------------------------------------------------


Get LanVpnInterfaceEthernet associated Tracker Parcel by trackerId for service feature profile

.. code:: python

    def get_lan_vpn_interface_ethernet_associated_tracker_parcel_by_parcel_id_for_transport(
        service_id: str, vpn_id: str, ethernet_id: str, tracker_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.tracker.get_lan_vpn_interface_ethernet_associated_tracker_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------------------------------------------------------


Update a LanVpnInterfaceEthernet parcel and a Tracker Parcel association for service feature profile

.. code:: python

    def edit_lan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport(
        service_id: str,
        vpn_id: str,
        ethernet_id: str,
        tracker_id: str,
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.tracker.edit_lan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ethernet/{ethernetId}/tracker/{trackerId}
-----------------------------------------------------------------------------------------------------------------------------------------------


Delete a LanVpnInterfaceEthernet and a Tracker Parcel association for service feature profile

.. code:: python

    def delete_lan_vpn_interface_ethernet_and_tracker_association_for_transport(
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.tracker.delete_lan_vpn_interface_ethernet_and_tracker_association_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnParcelId}/interface/ethernet/{ethernetId}/tracker
---------------------------------------------------------------------------------------------------------------------------------------


Associate a LanVpnInterfaceEthernet parcel with a Tracker Parcel for service feature profile

.. code:: python

    def create_lan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport(
        service_id: str,
        vpn_parcel_id: str,
        ethernet_id: str,
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ethernet.tracker.create_lan_vpn_interface_ethernet_and_tracker_parcel_association_for_transport()


