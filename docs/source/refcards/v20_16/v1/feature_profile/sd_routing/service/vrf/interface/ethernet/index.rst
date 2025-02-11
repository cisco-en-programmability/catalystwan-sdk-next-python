============================================================
v1.feature_profile.sd_routing.service.vrf.interface.ethernet
============================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet
------------------------------------------------------------------------------------------------------------


Get all ethernet interface features from a specific service VRF feature in service feature profile

.. code:: python

    def get_sdrouting_service_vrf_interface_ethernet_features_for_service(
        service_id: str, vrf_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.get_sdrouting_service_vrf_interface_ethernet_features_for_service()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet
-------------------------------------------------------------------------------------------------------------


Create a SD-Routing ethernet interface feature from a specific service VRF feature in service feature profile

.. code:: python

    def create_sdrouting_service_vrf_interface_ethernet_feature_for_service(
        service_id: str, vrf_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.create_sdrouting_service_vrf_interface_ethernet_feature_for_service()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}
-------------------------------------------------------------------------------------------------------------------------


Get the SD-Routing ethernet interface feature from a specific service VRF feature by feature ID in service feature profile

.. code:: python

    def get_sdrouting_service_vrf_interface_ethernet_feature_by_feature_id_for_service(
        service_id: str, vrf_id: str, ethernet_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.get_sdrouting_service_vrf_interface_ethernet_feature_by_feature_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}
-------------------------------------------------------------------------------------------------------------------------


Edit the SD-Routing ethernet interface feature from a specific service VRF feature in service feature profile

.. code:: python

    def edit_sdrouting_service_vrf_interface_ethernet_feature_for_service(
        service_id: str,
        vrf_id: str,
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.edit_sdrouting_service_vrf_interface_ethernet_feature_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}
----------------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing ethernet interface feature from a specific service VRF feature in service feature profile

.. code:: python

    def delete_sdrouting_service_vrf_interface_ethernet_feature_for_service(
        service_id: str, vrf_id: str, ethernet_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.delete_sdrouting_service_vrf_interface_ethernet_feature_for_service()


.. toctree::
    :maxdepth: 1

    dhcp_server

