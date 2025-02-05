=============================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular
=============================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular
---------------------------------------------------------------------------------------------------------------


Get Interface Cellular Parcels for transport Wan Vpn Parcel

.. code:: python

    def get_interface_cellular_parcels_for_transport_wan_vpn(
        transport_id: str, vpn_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.get_interface_cellular_parcels_for_transport_wan_vpn()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular
----------------------------------------------------------------------------------------------------------------


Create a wanvpn Cellular interface Parcel for transport feature profile

.. code:: python

    def create_wan_vpn_interface_cellular_parcel_for_transport(
        transport_id: str, vpn_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.create_wan_vpn_interface_cellular_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{intfId}
------------------------------------------------------------------------------------------------------------------------


Get wanvpn Cellular interface Parcel by intfId for transport feature profile

.. code:: python

    def get_wan_vpn_interface_cellular_parcel_by_parcel_id_for_transport(
        transport_id: str, vpn_id: str, intf_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.get_wan_vpn_interface_cellular_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{intfId}
------------------------------------------------------------------------------------------------------------------------


Update a wanvpn Cellular Interface Parcel for transport feature profile

.. code:: python

    def edit_wan_vpn_interface_cellular_parcel_for_transport(
        transport_id: str,
        vpn_id: str,
        intf_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.edit_wan_vpn_interface_cellular_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/cellular/{intfId}
---------------------------------------------------------------------------------------------------------------------------


Delete a wanvpn Cellular interface Parcel for transport feature profile

.. code:: python

    def delete_wan_vpn_interface_cellular_for_transport(
        transport_id: str, vpn_id: str, intf_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.cellular.delete_wan_vpn_interface_cellular_for_transport()


.. toctree::
    :maxdepth: 1

    schema/index
    ipv6_tracker
    ipv6_trackergroup
    tracker
    trackergroup

