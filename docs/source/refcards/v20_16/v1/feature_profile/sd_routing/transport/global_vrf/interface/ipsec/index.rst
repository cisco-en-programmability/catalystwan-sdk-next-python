==================================================================
v1.feature_profile.sd_routing.transport.global_vrf.interface.ipsec
==================================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/ipsec
---------------------------------------------------------------------------------------------------------------------


Create a SD-Routing IPSec interface feature in the global VRF from a specific transport feature profile

.. code:: python

    def post(
        transport_id: str,
        vrf_id: str,
        payload: CreateSdroutingTransportGlobalVrfInterfaceIpsecFeatureForTransportPostRequest,
    ) -> CreateSdroutingTransportGlobalVrfInterfaceIpsecFeatureForTransportPostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.ipsec.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/ipsec/{ipsecId}
------------------------------------------------------------------------------------------------------------------------------


Edit the SD-Routing IPSec interface feature in the global VRF from a specific transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vrf_id: str,
        ipsec_id: str,
        payload: EditSdroutingTransportGlobalVrfInterfaceIpsecFeatureForTransportPutRequest,
    ) -> EditSdroutingTransportGlobalVrfInterfaceIpsecFeatureForTransportPutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.ipsec.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/ipsec/{ipsecId}
---------------------------------------------------------------------------------------------------------------------------------


Delete the SD-Routing IPSec interface feature in the global VRF from a specific transport feature profile

.. code:: python

    def delete(transport_id: str, vrf_id: str, ipsec_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.ipsec.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/ipsec
--------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str
    ) -> GetListSdRoutingTransportGlobalVrfWanInterfaceIpsecPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.ipsec.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}/interface/ipsec/{ipsecId}
------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str, ipsec_id: str
    ) -> GetSingleSdRoutingTransportGlobalVrfWanInterfaceIpsecPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.interface.ipsec.get()


.. toctree::
    :maxdepth: 1

    models

