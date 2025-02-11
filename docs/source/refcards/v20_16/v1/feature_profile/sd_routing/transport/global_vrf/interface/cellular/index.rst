=====================================================================
v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular
=====================================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular
-----------------------------------------------------------------------------------------------------------------------


Get Global VRF Interface Cellular Features for transport Parcel

.. code:: python

    def get_global_vrf_interface_cellular_parcels_for_transport(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.get_global_vrf_interface_cellular_parcels_for_transport()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular
------------------------------------------------------------------------------------------------------------------------


Create a Global VRF Cellular interface Feature for transport feature profile

.. code:: python

    def create_global_vrf_interface_cellular_parcel_for_transport(
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.create_global_vrf_interface_cellular_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{intfId}
--------------------------------------------------------------------------------------------------------------------------------


Get Global VRF Cellular interface Feature by intfId for transport feature profile

.. code:: python

    def get_global_vrf_interface_cellular_parcel_by_parcel_id_for_transport(
        transport_id: str, vrf_id: str, intf_id: str
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.get_global_vrf_interface_cellular_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{intfId}
--------------------------------------------------------------------------------------------------------------------------------


Update a Global VRF Cellular Interface Feature for transport feature profile

.. code:: python

    def edit_global_vrf_interface_cellular_parcel_for_transport(
        transport_id: str,
        vrf_id: str,
        intf_id: str,
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.edit_global_vrf_interface_cellular_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/cellular/{intfId}
-----------------------------------------------------------------------------------------------------------------------------------


Delete a Global VRF Cellular interface Feature for transport feature profile

.. code:: python

    def delete_global_vrf_interface_cellular_for_transport(
        transport_id: str, vrf_id: str, intf_id: str
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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.cellular.delete_global_vrf_interface_cellular_for_transport()


.. toctree::
    :maxdepth: 1

    tracker
    trackergroup

