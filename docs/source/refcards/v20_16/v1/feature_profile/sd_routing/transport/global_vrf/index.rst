==================================================
v1.feature_profile.sd_routing.transport.global_vrf
==================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf
---------------------------------------------------------------------------------------------


Create a SD-Routing Global VRF feature from a specific transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateSdroutingTransportGlobalVrfFeaturePostRequest,
    ) -> CreateSdroutingTransportGlobalVrfFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}
----------------------------------------------------------------------------------------------------


Edit the SD-Routing Global VRF feature from a specific transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vrf_id: str,
        payload: EditSdroutingTransportGlobalVrfFeaturePutRequest,
    ) -> EditSdroutingTransportGlobalVrfFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}
-------------------------------------------------------------------------------------------------------


Delete the SD-Routing Global VRF feature from a specific transport feature profile

.. code:: python

    def delete(transport_id: str, vrf_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf
--------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdRoutingTransportGlobalVrfPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/global-vrf/{vrfId}
----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str
    ) -> GetSingleSdRoutingTransportGlobalVrfPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.global_vrf.get()


.. toctree::
    :maxdepth: 1

    routing/index
    interface/index
    multicloud_connection/index
    models

