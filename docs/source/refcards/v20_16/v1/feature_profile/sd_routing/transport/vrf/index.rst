===========================================
v1.feature_profile.sd_routing.transport.vrf
===========================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf
--------------------------------------------------------------------------------------


Create a SD-Routing VRF feature from a specific transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateSdroutingTransportVrfFeaturePostRequest,
    ) -> CreateSdroutingTransportVrfFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.vrf.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}
---------------------------------------------------------------------------------------------


Edit the SD-Routing VRF feature from a specific transport feature profile

.. code:: python

    def put(
        transport_id: str,
        vrf_id: str,
        payload: EditSdroutingTransportVrfFeaturePutRequest,
    ) -> EditSdroutingTransportVrfFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.vrf.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}
------------------------------------------------------------------------------------------------


Delete the SD-Routing VRF feature from a specific transport feature profile

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
        client.v1.feature_profile.sd_routing.transport.vrf.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf
-------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(transport_id: str) -> GetListSdRoutingTransportVrfPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.vrf.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/vrf/{vrfId}
---------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str
    ) -> GetSingleSdRoutingTransportVrfPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.vrf.get()


.. toctree::
    :maxdepth: 1

    routing/index
    interface/index
    models

