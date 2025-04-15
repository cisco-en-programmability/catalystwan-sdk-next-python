========================================================================
v1.feature_profile.sd_routing.service.vrf.interface.ethernet.dhcp_server
========================================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server
--------------------------------------------------------------------------------------------------------------------------------------


Associate a SD-Routing VRF Interface Ethernet feature with a DHCP Server feature for service feature profile

.. code:: python

    def post(
        service_id: str,
        vrf_id: str,
        ethernet_id: str,
        payload: CreateVrfInterfaceEthernetAndDhcpServerParcelAssociationForServicePostRequest,
    ) -> CreateVrfInterfaceEthernetAndDhcpServerParcelAssociationForServicePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.dhcp_server.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server/{dhcpServerId}
----------------------------------------------------------------------------------------------------------------------------------------------------


Update a SD-Routing VRF Interface Ethernet feature and a DHCP Server feature association for service feature profile

.. code:: python

    def put(
        service_id: str,
        vrf_id: str,
        ethernet_id: str,
        dhcp_server_id: str,
        payload: EditVrfInterfaceEthernetAndDhcpServerParcelAssociationForServicePutRequest,
    ) -> EditVrfInterfaceEthernetAndDhcpServerParcelAssociationForServicePutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.dhcp_server.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server/{dhcpServerId}
-------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a VRF Interface Ethernet feature and a DHCP Server feature association for service feature profile

.. code:: python

    def delete(
        service_id: str,
        vrf_id: str,
        ethernet_id: str,
        dhcp_server_id: str,
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.dhcp_server.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server
-------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str, ethernet_id: str
    ) -> List[
        GetVrfInterfaceEthernetAssociatedDhcpServerParcelsForServiceGetResponse
    ]: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.dhcp_server.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}/dhcp-server/{dhcpServerId}
----------------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
        vrf_id: str,
        ethernet_id: str,
        dhcp_server_id: str,
    ) -> (
        GetSingleSdRoutingServiceVrfInterfaceEthernetDhcpServerPayload
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.dhcp_server.get()


.. toctree::
    :maxdepth: 1

    models

