=========================================
v1.feature_profile.sd_routing.service.vrf
=========================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf
----------------------------------------------------------------------------------


Create a SD-Routing VRF feature from a specific service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateSdroutingServiceVrfFeaturePostRequest,
    ) -> CreateSdroutingServiceVrfFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}
-----------------------------------------------------------------------------------------


Edit the SD-Routing VRF feature from a specific service feature profile

.. code:: python

    def put(
        service_id: str,
        vrf_id: str,
        payload: EditSdroutingServiceVrfFeaturePutRequest,
    ) -> EditSdroutingServiceVrfFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}
--------------------------------------------------------------------------------------------


Delete the SD-Routing VRF feature from a specific service feature profile

.. code:: python

    def delete(service_id: str, vrf_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf
---------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(service_id: str) -> GetListSdRoutingServiceVrfPayload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/vrf/{vrfId}
-----------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, vrf_id: str
    ) -> GetSingleSdRoutingServiceVrfPayload: ...


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
        client.v1.feature_profile.sd_routing.service.vrf.get()


.. toctree::
    :maxdepth: 1

    routing/index
    dmvpn_tunnel/index
    interface/index
    models

