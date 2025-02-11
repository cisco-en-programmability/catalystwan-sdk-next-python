========================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.gre
========================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre
----------------------------------------------------------------------------------------------------------


Get InterfaceGre Parcels for transport WanVpn Parcel

.. code:: python

    def get_interface_gre_parcels_for_transport_wan_vpn(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.get_interface_gre_parcels_for_transport_wan_vpn()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre
-----------------------------------------------------------------------------------------------------------


Create a WanVpn InterfaceGre parcel for transport feature profile

.. code:: python

    def create_wan_vpn_interface_gre_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.create_wan_vpn_interface_gre_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}
------------------------------------------------------------------------------------------------------------------


Get WanVpn InterfaceGre Parcel by greId for transport feature profile

.. code:: python

    def get_wan_vpn_interface_gre_parcel_by_parcel_id_for_transport(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.get_wan_vpn_interface_gre_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}
------------------------------------------------------------------------------------------------------------------


Update a WanVpn InterfaceGre Parcel for transport feature profile

.. code:: python

    def edit_wan_vpn_interface_gre_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.edit_wan_vpn_interface_gre_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/gre/{greId}
---------------------------------------------------------------------------------------------------------------------


Delete a  WanVpn InterfaceGre Parcel for transport feature profile

.. code:: python

    def delete_wan_vpn_interface_gre_for_transport(
        transport_id: str, vpn_id: str, gre_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.gre.delete_wan_vpn_interface_gre_for_transport()


.. toctree::
    :maxdepth: 1

    schema/index
    tracker

