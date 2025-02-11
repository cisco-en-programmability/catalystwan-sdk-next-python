================================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.tracker
================================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker
--------------------------------------------------------------------------------------------------------------------------


Get WanVpnInterfaceGre associated Tracker Parcels for transport feature profile

.. code:: python

    def get_wan_vpn_interface_gre_associated_tracker_parcels_for_transport(
        transport_id: str, vpn_id: str, gre_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.tracker.get_wan_vpn_interface_gre_associated_tracker_parcels_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker
---------------------------------------------------------------------------------------------------------------------------


Associate a WanVpnInterfaceGre parcel with a Tracker Parcel for transport feature profile

.. code:: python

    def create_wan_vpn_interface_gre_and_tracker_parcel_association_for_transport(
        transport_id: str,
        vpn_id: str,
        gre_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.tracker.create_wan_vpn_interface_gre_and_tracker_parcel_association_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------------------------------------------------


Get WanVpnInterfaceGre associated Tracker Parcel by trackerId for transport feature profile

.. code:: python

    def get_wan_vpn_interface_gre_associated_tracker_parcel_by_parcel_id_for_transport(
        transport_id: str, vpn_id: str, gre_id: str, tracker_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.tracker.get_wan_vpn_interface_gre_associated_tracker_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker/{trackerId}
--------------------------------------------------------------------------------------------------------------------------------------


Update a WanVpnInterfaceGre parcel and a Tracker Parcel association for transport feature profile

.. code:: python

    def edit_wan_vpn_interface_gre_and_tracker_parcel_association_for_transport(
        transport_id: str,
        vpn_id: str,
        gre_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.tracker.edit_wan_vpn_interface_gre_and_tracker_parcel_association_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}/tracker/{trackerId}
-----------------------------------------------------------------------------------------------------------------------------------------


Delete a WanVpnInterfaceGre and a Tracker Parcel association for transport feature profile

.. code:: python

    def delete_wan_vpn_interface_gre_and_tracker_association_for_transport(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.tracker.delete_wan_vpn_interface_gre_and_tracker_association_for_transport()


