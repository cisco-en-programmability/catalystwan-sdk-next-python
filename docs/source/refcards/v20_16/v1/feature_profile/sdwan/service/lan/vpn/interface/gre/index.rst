======================================================
v1.feature_profile.sdwan.service.lan.vpn.interface.gre
======================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/gre
------------------------------------------------------------------------------------------------------


Get InterfaceGre for service LanVpn

.. code:: python

    def get_interface_gres_for_service_lan_vpn(
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.gre.get_interface_gres_for_service_lan_vpn()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/gre
-------------------------------------------------------------------------------------------------------


Create a LanVpn InterfaceGre for service feature profile

.. code:: python

    def create_lan_vpn_interface_gre_for_service(
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.gre.create_lan_vpn_interface_gre_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/gre/{greId}
--------------------------------------------------------------------------------------------------------------


Get LanVpn InterfaceGre by greId for service feature profile

.. code:: python

    def get_lan_vpn_interface_gre_by_id_for_service(
        service_id: str, vpn_id: str, gre_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.gre.get_lan_vpn_interface_gre_by_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/gre/{greId}
--------------------------------------------------------------------------------------------------------------


Update a LanVpn InterfaceGre Feature for service feature profile

.. code:: python

    def edit_lan_vpn_interface_gre_for_service(
        service_id: str,
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.gre.edit_lan_vpn_interface_gre_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/lan/vpn/{vpnId}/interface/gre/{greId}
-----------------------------------------------------------------------------------------------------------------


Delete a  LanVpn InterfaceGre for service feature profile

.. code:: python

    def delete_lan_vpn_interface_gre_for_service(
        service_id: str, vpn_id: str, gre_id: str
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
        client.v1.feature_profile.sdwan.service.lan.vpn.interface.gre.delete_lan_vpn_interface_gre_for_service()


.. toctree::
    :maxdepth: 1

    schema/index

