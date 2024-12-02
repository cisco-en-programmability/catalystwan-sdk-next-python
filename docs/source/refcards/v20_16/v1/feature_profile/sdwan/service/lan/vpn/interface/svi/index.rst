======================================================
v1.feature_profile.sdwan.service.lan.vpn.interface.svi
======================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi
------------------------------------------------------------------------------------------------------


Get InterfaceSvi Parcels for service LanVpn Parcel

.. code:: python

    def get_interface_svi_parcels_for_service_lan_vpn(
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.svi.get_interface_svi_parcels_for_service_lan_vpn()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi
-------------------------------------------------------------------------------------------------------


Create a LanVpn InterfaceSvi parcel for service feature profile

.. code:: python

    def create_lan_vpn_interface_svi_parcel_for_service(
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.svi.create_lan_vpn_interface_svi_parcel_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}
--------------------------------------------------------------------------------------------------------------


Get LanVpn InterfaceSvi Parcel by sviId for service feature profile

.. code:: python

    def get_lan_vpn_interface_svi_parcel_by_parcel_id_for_service(
        service_id: str, vpn_id: str, svi_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.svi.get_lan_vpn_interface_svi_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}
--------------------------------------------------------------------------------------------------------------


Update a LanVpn InterfaceSvi Parcel for service feature profile

.. code:: python

    def edit_lan_vpn_interface_svi_parcel_for_service(
        service_id: str,
        vpn_id: str,
        svi_id: str,
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.svi.edit_lan_vpn_interface_svi_parcel_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/svi/{sviId}
-----------------------------------------------------------------------------------------------------------------


Delete a  LanVpn InterfaceSvi Parcel for service feature profile

.. code:: python

    def delete_lan_vpn_interface_svi_for_service(
        service_id: str, vpn_id: str, svi_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.svi.delete_lan_vpn_interface_svi_for_service()


.. toctree::
    :maxdepth: 1

    schema/index
    dhcp_server

