==========================================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.trackergroup
==========================================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup
-----------------------------------------------------------------------------------------------------------------------------------------


Get WanVpnInterfaceEthernet associated TrackerGroup Parcels for transport feature profile

.. code:: python

    def get_wan_vpn_interface_ethernet_associated_tracker_group_parcels_for_transport(
        transport_id: str, vpn_id: str, ethernet_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.trackergroup.get_wan_vpn_interface_ethernet_associated_tracker_group_parcels_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup/{trackergroupId}
----------------------------------------------------------------------------------------------------------------------------------------------------------


Get WanVpnInterfaceEthernet associated TrackerGroup Parcel by trackergroupId for transport feature profile

.. code:: python

    def get_wan_vpn_interface_ethernet_associated_tracker_group_parcel_by_parcel_id_for_transport(
        transport_id: str,
        vpn_id: str,
        ethernet_id: str,
        trackergroup_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.trackergroup.get_wan_vpn_interface_ethernet_associated_tracker_group_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup/{trackergroupId}
----------------------------------------------------------------------------------------------------------------------------------------------------------


Update a WanVpnInterfaceEthernet parcel and a TrackerGroup Parcel association for transport feature profile

.. code:: python

    def edit_wan_vpn_interface_ethernet_and_tracker_group_parcel_association_for_transport(
        transport_id: str,
        vpn_id: str,
        ethernet_id: str,
        trackergroup_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.trackergroup.edit_wan_vpn_interface_ethernet_and_tracker_group_parcel_association_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ethernet/{ethernetId}/trackergroup/{trackergroupId}
-------------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a WanVpnInterfaceEthernet and a TrackerGroup Parcel association for transport feature profile

.. code:: python

    def delete_wan_vpn_interface_ethernet_and_tracker_group_association_for_transport(
        transport_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.trackergroup.delete_wan_vpn_interface_ethernet_and_tracker_group_association_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnParcelId}/interface/ethernet/{ethernetId}/trackergroup
------------------------------------------------------------------------------------------------------------------------------------------------


Associate a WanVpnInterfaceEthernet parcel with a TrackerGroup Parcel for transport feature profile

.. code:: python

    def create_wan_vpn_interface_ethernet_and_tracker_group_parcel_association_for_transport(
        transport_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ethernet.trackergroup.create_wan_vpn_interface_ethernet_and_tracker_group_parcel_association_for_transport()


