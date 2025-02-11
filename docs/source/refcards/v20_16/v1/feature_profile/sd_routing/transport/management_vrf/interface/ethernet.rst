=========================================================================
v1.feature_profile.sd_routing.transport.management_vrf.interface.ethernet
=========================================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet
---------------------------------------------------------------------------------------------------------------------------


Get all  Management Ethernet interface features from a specific management VRF feature in Transport Feature Profile

.. code:: python

    def get_sdrouting_management_vrf_interface_ethernet_parcels_for_transport_profile(
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
        client.v1.feature_profile.sd_routing.transport.management_vrf.interface.ethernet.get_sdrouting_management_vrf_interface_ethernet_parcels_for_transport_profile()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet
----------------------------------------------------------------------------------------------------------------------------


Create a SD-Routing Management Ethernet interface feature from a specific management VRF feature in Transport Feature Profile

.. code:: python

    def create_sdrouting_management_vrf_interface_ethernet_parcel_for_transport_profile(
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
        client.v1.feature_profile.sd_routing.transport.management_vrf.interface.ethernet.create_sdrouting_management_vrf_interface_ethernet_parcel_for_transport_profile()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet/{ethernetId}
----------------------------------------------------------------------------------------------------------------------------------------


Get the SD-Routing Management Ethernet interface feature from a specific management VRF feature by ethernetId in Transport Feature Profile

.. code:: python

    def get_sdrouting_management_vrf_interface_ethernet_parcel_by_parcel_id_for_transport_profile(
        transport_id: str, vrf_id: str, ethernet_id: str
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
        client.v1.feature_profile.sd_routing.transport.management_vrf.interface.ethernet.get_sdrouting_management_vrf_interface_ethernet_parcel_by_parcel_id_for_transport_profile()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet/{ethernetId}
----------------------------------------------------------------------------------------------------------------------------------------


Edit the SD-Routing Management Ethernet interface feature from a specific management VRF feature in Transport Feature Profile

.. code:: python

    def edit_sdrouting_management_vrf_interface_ethernet_parcel_for_transport_profile(
        transport_id: str,
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
        client.v1.feature_profile.sd_routing.transport.management_vrf.interface.ethernet.edit_sdrouting_management_vrf_interface_ethernet_parcel_for_transport_profile()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet/{ethernetId}
-------------------------------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing Management Ethernet interface feature from a specific management VRF feature in Transport Feature Profile

.. code:: python

    def delete_sdrouting_management_vrf_interface_ethernet_parcel_for_transport_profile(
        transport_id: str, vrf_id: str, ethernet_id: str
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
        client.v1.feature_profile.sd_routing.transport.management_vrf.interface.ethernet.delete_sdrouting_management_vrf_interface_ethernet_parcel_for_transport_profile()


