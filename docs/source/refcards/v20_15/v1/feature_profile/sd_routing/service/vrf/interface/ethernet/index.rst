============================================================
v1.feature_profile.sd_routing.service.vrf.interface.ethernet
============================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet
-------------------------------------------------------------------------------------------------------------


Create a SD-Routing Ethernet interface feature for VRF in Service Feature Profile

.. code:: python

    def post(
        service_id: str,
        vrf_id: str,
        payload: CreateSdroutingServiceVrfInterfaceEthernetParcelForServicePostRequest,
    ) -> CreateSdroutingServiceVrfInterfaceEthernetParcelForServicePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}
-------------------------------------------------------------------------------------------------------------------------


Edit a SD-Routing Ethernet interface feature for VRF in Service Feature Profile

.. code:: python

    def put(
        service_id: str,
        vrf_id: str,
        ethernet_id: str,
        payload: EditSdroutingServiceVrfInterfaceEthernetParcelForServicePutRequest,
    ) -> EditSdroutingServiceVrfInterfaceEthernetParcelForServicePutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}
----------------------------------------------------------------------------------------------------------------------------


Delete a SD-Routing Ethernet interface feature for VRF in Service Feature Profile

.. code:: python

    def delete(
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet
------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str
    ) -> GetListSdRoutingServiceVrfLanInterfaceEthernetPayload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ethernet/{ethernetId}
-------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str, ethernet_id: str
    ) -> GetSingleSdRoutingServiceVrfLanInterfaceEthernetPayload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ethernet.get()


.. toctree::
    :maxdepth: 1

    dhcp_server/index
    models

