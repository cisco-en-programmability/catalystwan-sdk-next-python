==========================================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_tracker
==========================================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-tracker
-----------------------------------------------------------------------------------------------------------------------------------------


Get WanVpnInterfaceCellular associated IPv6 Tracker Parcels for transport feature profile

.. code:: python

    def get_wan_vpn_interface_cellular_associated_ipv6_tracker_parcels_for_transport(
        transport_id: str, vpn_id: str, cellular_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_tracker.get_wan_vpn_interface_cellular_associated_ipv6_tracker_parcels_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-tracker/{ipv6-trackerId}
----------------------------------------------------------------------------------------------------------------------------------------------------------


Get WanVpnInterfaceCellular associated IPv6 Tracker Parcel by ipv6-trackerId for transport feature profile

.. code:: python

    def get_wan_vpn_interface_cellular_associated_ipv6_tracker_parcel_by_parcel_id_for_transport(
        transport_id: str,
        vpn_id: str,
        cellular_id: str,
        ipv6_tracker_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_tracker.get_wan_vpn_interface_cellular_associated_ipv6_tracker_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-tracker/{ipv6-trackerId}
----------------------------------------------------------------------------------------------------------------------------------------------------------


Update a WanVpnInterfaceCellular parcel and a IPv6 Tracker Parcel association for transport feature profile

.. code:: python

    def edit_wan_vpn_interface_cellular_and_ipv6_tracker_parcel_association_for_transport(
        transport_id: str,
        vpn_id: str,
        cellular_id: str,
        ipv6_tracker_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_tracker.edit_wan_vpn_interface_cellular_and_ipv6_tracker_parcel_association_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{cellularId}/ipv6-tracker/{ipv6-trackerId}
-------------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a WanVpnInterfaceCellular and a IPv6 Tracker Parcel association for transport feature profile

.. code:: python

    def delete_wan_vpn_interface_cellular_and_ipv6_tracker_association_for_transport(
        transport_id: str,
        vpn_id: str,
        cellular_id: str,
        ipv6_tracker_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_tracker.delete_wan_vpn_interface_cellular_and_ipv6_tracker_association_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnParcelId}/interface/cellular/{cellularId}/ipv6-tracker
------------------------------------------------------------------------------------------------------------------------------------------------


Associate a WanVpnInterfaceCellular parcel with a IPv6 Tracker Parcel for transport feature profile

.. code:: python

    def create_wan_vpn_interface_cellular_and_ipv6_tracker_parcel_association_for_transport(
        transport_id: str,
        vpn_parcel_id: str,
        cellular_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.ipv6_tracker.create_wan_vpn_interface_cellular_and_ipv6_tracker_parcel_association_for_transport()


