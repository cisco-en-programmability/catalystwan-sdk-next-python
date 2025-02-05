===========================================================
v1.feature_profile.sd_routing.transport.vrf.interface.ipsec
===========================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ipsec
-------------------------------------------------------------------------------------------------------------


Get all  IPSec interface features in a specific transport VRF from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_vrf_interface_ipsec_features_for_transport(
        transport_id: str, vrf_id: str
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
        client.v1.feature_profile.sd_routing.transport.vrf.interface.ipsec.get_sdrouting_transport_vrf_interface_ipsec_features_for_transport()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ipsec
--------------------------------------------------------------------------------------------------------------


Create a SD-Routing IPSec interface feature in a specific transport VRF from a specific transport feature profile

.. code:: python

    def create_sdrouting_transport_vrf_interface_ipsec_feature_for_transport(
        transport_id: str, vrf_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.transport.vrf.interface.ipsec.create_sdrouting_transport_vrf_interface_ipsec_feature_for_transport()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ipsec/{ipsecId}
-----------------------------------------------------------------------------------------------------------------------


Get the SD-Routing IPSec interface feature in a specific transport VRF from a specific transport feature profile

.. code:: python

    def get_sdrouting_transport_vrf_interface_ipsec_feature_by_feature_id_for_transport(
        transport_id: str, vrf_id: str, ipsec_id: str
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
        client.v1.feature_profile.sd_routing.transport.vrf.interface.ipsec.get_sdrouting_transport_vrf_interface_ipsec_feature_by_feature_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ipsec/{ipsecId}
-----------------------------------------------------------------------------------------------------------------------


Edit the SD-Routing IPSec interface feature in a specific transport VRF from a specific transport feature profile

.. code:: python

    def edit_sdrouting_transport_vrf_interface_ipsec_feature_for_transport(
        transport_id: str,
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
        client.v1.feature_profile.sd_routing.transport.vrf.interface.ipsec.edit_sdrouting_transport_vrf_interface_ipsec_feature_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}/interface/ipsec/{ipsecId}
--------------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing IPSec interface feature in a specific transport VRF from a specific transport feature profile

.. code:: python

    def delete_sdrouting_transport_vrf_interface_ipsec_feature_for_transport(
        transport_id: str, vrf_id: str, ipsec_id: str
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
        client.v1.feature_profile.sd_routing.transport.vrf.interface.ipsec.delete_sdrouting_transport_vrf_interface_ipsec_feature_for_transport()


