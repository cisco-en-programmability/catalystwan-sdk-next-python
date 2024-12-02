=========================================================
v1.feature_profile.sd_routing.service.vrf.interface.ipsec
=========================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ipsec
---------------------------------------------------------------------------------------------------------


Get all  IPSec interface features in a specific service VRF from a specific service feature profile

.. code:: python

    def get_sdrouting_service_vrf_interface_ipsec_features_for_service(
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ipsec.get_sdrouting_service_vrf_interface_ipsec_features_for_service()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ipsec
----------------------------------------------------------------------------------------------------------


Create a SD-Routing IPSec interface feature in a specific service VRF from a specific service feature profile

.. code:: python

    def create_sdrouting_service_vrf_interface_ipsec_feature_for_service(
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ipsec.create_sdrouting_service_vrf_interface_ipsec_feature_for_service()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ipsec/{ipsecId}
-------------------------------------------------------------------------------------------------------------------


Get the SD-Routing IPSec interface feature in a specific service VRF from a specific service feature profile

.. code:: python

    def get_sdrouting_service_vrf_interface_ipsec_feature_by_feature_id_for_service(
        service_id: str, vrf_id: str, ipsec_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ipsec.get_sdrouting_service_vrf_interface_ipsec_feature_by_feature_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ipsec/{ipsecId}
-------------------------------------------------------------------------------------------------------------------


Edit the SD-Routing IPSec interface feature in a specific service VRF from a specific service feature profile

.. code:: python

    def edit_sdrouting_service_vrf_interface_ipsec_feature_for_service(
        service_id: str,
        vrf_id: str,
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ipsec.edit_sdrouting_service_vrf_interface_ipsec_feature_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ipsec/{ipsecId}
----------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing IPSec interface feature in a specific service VRF from a specific service feature profile

.. code:: python

    def delete_sdrouting_service_vrf_interface_ipsec_feature_for_service(
        service_id: str, vrf_id: str, ipsec_id: str
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ipsec.delete_sdrouting_service_vrf_interface_ipsec_feature_for_service()


