====================================================
v1.feature_profile.sd_routing.transport.routing.ospf
====================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospf
-----------------------------------------------------------------------------------------------


Create a SD-Routing WAN OSPF feature from a specific transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateSdroutingTransportRoutingOspfFeaturePostRequest,
    ) -> CreateSdroutingTransportRoutingOspfFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospf.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospf/{ospfId}
-------------------------------------------------------------------------------------------------------


Edit the SD-Routing WAN OSPF feature from a specific transport feature profile

.. code:: python

    def put(
        transport_id: str,
        ospf_id: str,
        payload: EditSdroutingTransportRoutingOspfFeaturePutRequest,
    ) -> EditSdroutingTransportRoutingOspfFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospf.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospf/{ospfId}
----------------------------------------------------------------------------------------------------------


Delete the SD-Routing WAN OSPF feature from a specific transport feature profile

.. code:: python

    def delete(transport_id: str, ospf_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospf.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospf
----------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdRoutingTransportRoutingOspfPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospf.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/routing/ospf/{ospfId}
-------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, ospf_id: str
    ) -> GetSingleSdRoutingTransportRoutingOspfPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.routing.ospf.get()


.. toctree::
    :maxdepth: 1

    models

