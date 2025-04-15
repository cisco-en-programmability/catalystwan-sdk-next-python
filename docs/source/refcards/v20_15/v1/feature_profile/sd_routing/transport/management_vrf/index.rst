======================================================
v1.feature_profile.sd_routing.transport.management_vrf
======================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf
-------------------------------------------------------------------------------------------------


Create a SD-Routing Management VRF Feature for Transport Feature Profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateSdroutingManagementVrfFeaturePostRequest,
    ) -> CreateSdroutingManagementVrfFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.management_vrf.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}
--------------------------------------------------------------------------------------------------------


Edit a SD-Routing Management VRF Feature for Transport Feature Profile

.. code:: python

    def put(
        transport_id: str,
        vrf_id: str,
        payload: EditSdroutingManagementVrfFeaturePutRequest,
    ) -> EditSdroutingManagementVrfFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.management_vrf.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}
-----------------------------------------------------------------------------------------------------------


Delete a SD-Routing Management VRF Feature for Transport Feature Profile

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
        client.v1.feature_profile.sd_routing.transport.management_vrf.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf
------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdRoutingTransportManagementVrfPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.management_vrf.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/management-vrf/{vrfId}
--------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, vrf_id: str
    ) -> GetSingleSdRoutingTransportManagementVrfPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.management_vrf.get()


.. toctree::
    :maxdepth: 1

    interface/index
    models

