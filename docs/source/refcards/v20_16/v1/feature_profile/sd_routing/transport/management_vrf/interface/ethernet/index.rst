=========================================================================
v1.feature_profile.sd_routing.transport.management_vrf.interface.ethernet
=========================================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet
----------------------------------------------------------------------------------------------------------------------------


Create a SD-Routing Management Ethernet interface feature from a specific management VRF feature in Transport Feature Profile

.. code:: python

    def post(
        transport_id: str,
        vrf_id: str,
        payload: CreateSdroutingManagementVrfInterfaceEthernetParcelForTransportProfilePostRequest,
    ) -> CreateSdroutingManagementVrfInterfaceEthernetParcelForTransportProfilePostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.management_vrf.interface.ethernet.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet/{ethernetId}
----------------------------------------------------------------------------------------------------------------------------------------


Edit the SD-Routing Management Ethernet interface feature from a specific management VRF feature in Transport Feature Profile

.. code:: python

    def put(
        transport_id: str,
        vrf_id: str,
        ethernet_id: str,
        payload: EditSdroutingManagementVrfInterfaceEthernetParcelForTransportProfilePutRequest,
    ) -> EditSdroutingManagementVrfInterfaceEthernetParcelForTransportProfilePutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.management_vrf.interface.ethernet.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet/{ethernetId}
-------------------------------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing Management Ethernet interface feature from a specific management VRF feature in Transport Feature Profile

.. code:: python

    def delete(
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
        client.v1.feature_profile.sd_routing.transport.management_vrf.interface.ethernet.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet
---------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str
    ) -> (
        GetListSdRoutingTransportManagementVrfInterfaceEthernetPayload
    ): ...


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
        client.v1.feature_profile.sd_routing.transport.management_vrf.interface.ethernet.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}/interface/ethernet/{ethernetId}
----------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str, ethernet_id: str
    ) -> (
        GetSingleSdRoutingTransportManagementVrfInterfaceEthernetPayload
    ): ...


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
        client.v1.feature_profile.sd_routing.transport.management_vrf.interface.ethernet.get()


.. toctree::
    :maxdepth: 1

    models

