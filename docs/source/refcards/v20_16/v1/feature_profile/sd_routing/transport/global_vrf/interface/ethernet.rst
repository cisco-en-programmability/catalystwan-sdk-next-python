=====================================================================
v1.feature_profile.sd_routing.transport.global_vrf.interface.ethernet
=====================================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/ethernet
-----------------------------------------------------------------------------------------------------------------------


Get all  Ethernet interface profile features from a specific global VRF feature in Transport Feature Profile

.. code:: python

    def get_sdrouting_transport_global_vrf_interface_ethernet_parcels_for_transport(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.ethernet.get_sdrouting_transport_global_vrf_interface_ethernet_parcels_for_transport()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/ethernet
------------------------------------------------------------------------------------------------------------------------


Create a SD-Routing Ethernet interface profile feature from a specific global VRF feature in Transport Feature Profile

.. code:: python

    def create_sdrouting_transport_global_vrf_interface_ethernet_parcel_for_transport(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.ethernet.create_sdrouting_transport_global_vrf_interface_ethernet_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/ethernet/{ethernetId}
------------------------------------------------------------------------------------------------------------------------------------


Get the SD-Routing Ethernet interface profile feature from a specific global VRF feature by ethernetId in Transport Feature Profile

.. code:: python

    def get_sdrouting_transport_global_vrf_interface_ethernet_parcel_by_parcel_id_for_transport(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.ethernet.get_sdrouting_transport_global_vrf_interface_ethernet_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/ethernet/{ethernetId}
------------------------------------------------------------------------------------------------------------------------------------


Edit the SD-Routing Ethernet interface profile feature from a specific global VRF feature in Transport Feature Profile

.. code:: python

    def edit_sdrouting_transport_global_vrf_interface_ethernet_parcel_for_transport(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.ethernet.edit_sdrouting_transport_global_vrf_interface_ethernet_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/ethernet/{ethernetId}
---------------------------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing Ethernet interface profile feature from a specific global VRF feature in Transport Feature Profile

.. code:: python

    def delete_sdrouting_transport_global_vrf_interface_ethernet_parcel_for_transport(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.ethernet.delete_sdrouting_transport_global_vrf_interface_ethernet_parcel_for_transport()


