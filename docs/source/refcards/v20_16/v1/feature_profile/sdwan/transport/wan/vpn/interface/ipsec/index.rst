==========================================================
v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec
==========================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec
------------------------------------------------------------------------------------------------------------


Get InterfaceIpsec Parcels for transport WanVpn Parcel

.. code:: python

    def get_list_of_profile_parcels_1(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.get_list_of_profile_parcels_1()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec
-------------------------------------------------------------------------------------------------------------


Create a WanVpn InterfaceIpsec parcel for transport feature profile

.. code:: python

    def create_ip_sec_profile_parcel_1(
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.create_ip_sec_profile_parcel_1()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec/{ipsecId}
----------------------------------------------------------------------------------------------------------------------


Get WanVpn InterfaceIpsec Parcel by ethernetId for transport feature profile

.. code:: python

    def get_profile_parcel_by_parcel_id_1(
        transport_id: str, vpn_id: str, ipsec_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.get_profile_parcel_by_parcel_id_1()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec/{ipsecId}
----------------------------------------------------------------------------------------------------------------------


Update a WanVpn InterfaceIpsec Parcel for transport feature profile

.. code:: python

    def edit_profile_parcel_1(
        transport_id: str,
        vpn_id: str,
        ipsec_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.edit_profile_parcel_1()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}/interface/ipsec/{ipsecId}
-------------------------------------------------------------------------------------------------------------------------


Delete a  WanVpn InterfaceIpsec Parcel for transport feature profile

.. code:: python

    def delete_profile_parcel_1(
        transport_id: str, vpn_id: str, ipsec_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.interface.ipsec.delete_profile_parcel_1()


.. toctree::
    :maxdepth: 1

    schema/index
    tracker

