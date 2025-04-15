=========================================================
v1.feature_profile.sd_routing.service.vrf.interface.ipsec
=========================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ipsec
----------------------------------------------------------------------------------------------------------


Create a SD-Routing IPSec interface feature in a specific service VRF from a specific service feature profile

.. code:: python

    def post(
        service_id: str,
        vrf_id: str,
        payload: CreateSdroutingServiceVrfInterfaceIpsecFeatureForServicePostRequest,
    ) -> CreateSdroutingServiceVrfInterfaceIpsecFeatureForServicePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ipsec.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ipsec/{ipsecId}
-------------------------------------------------------------------------------------------------------------------


Edit the SD-Routing IPSec interface feature in a specific service VRF from a specific service feature profile

.. code:: python

    def put(
        service_id: str,
        vrf_id: str,
        ipsec_id: str,
        payload: EditSdroutingServiceVrfInterfaceIpsecFeatureForServicePutRequest,
    ) -> (
        EditSdroutingServiceVrfInterfaceIpsecFeatureForServicePutResponse
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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ipsec.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ipsec/{ipsecId}
----------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing IPSec interface feature in a specific service VRF from a specific service feature profile

.. code:: python

    def delete(service_id: str, vrf_id: str, ipsec_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ipsec.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ipsec
---------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str
    ) -> GetListSdRoutingServiceVrfLanInterfaceIpsecPayload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ipsec.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}/interface/ipsec/{ipsecId}
-------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str, ipsec_id: str
    ) -> GetSingleSdRoutingServiceVrfLanInterfaceIpsecPayload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.interface.ipsec.get()


.. toctree::
    :maxdepth: 1

    models

