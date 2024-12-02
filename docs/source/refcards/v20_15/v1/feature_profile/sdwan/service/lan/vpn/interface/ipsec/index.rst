========================================================
v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec
========================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec
--------------------------------------------------------------------------------------------------------


Get InterfaceIpsec Parcels for Service LanVpn Parcel

.. code:: python

    def get_list_of_profile_parcels(
        service_id: str, vpn_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.get_list_of_profile_parcels()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec
---------------------------------------------------------------------------------------------------------


Create a LanVpn InterfaceIpsec parcel for service feature profile

.. code:: python

    def create_ip_sec_profile_parcel(
        service_id: str, vpn_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.create_ip_sec_profile_parcel()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}
------------------------------------------------------------------------------------------------------------------


Get LanVpn InterfaceIpsec Parcel by ethernetId for Service feature profile

.. code:: python

    def get_profile_parcel_by_parcel_id(
        service_id: str, vpn_id: str, ipsec_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.get_profile_parcel_by_parcel_id()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}
------------------------------------------------------------------------------------------------------------------


Update a LanVpn Interface Ipsec Parcel for Service feature profile

.. code:: python

    def edit_profile_parcel(
        service_id: str,
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.edit_profile_parcel()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/ipsec/{ipsecId}
---------------------------------------------------------------------------------------------------------------------


Delete a  LanVpn InterfaceIpsec Parcel for Service feature profile

.. code:: python

    def delete_profile_parcel(
        service_id: str, vpn_id: str, ipsec_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.ipsec.delete_profile_parcel()


.. toctree::
    :maxdepth: 1

    schema/index
    dhcp_server

