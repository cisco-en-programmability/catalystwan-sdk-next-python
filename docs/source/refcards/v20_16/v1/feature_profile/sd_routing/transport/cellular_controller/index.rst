===========================================================
v1.feature_profile.sd_routing.transport.cellular_controller
===========================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller
------------------------------------------------------------------------------------------------------


Create a Cellular Controller Profile Feature for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateCellularControllerProfileParcelForTransport1PostRequest,
    ) -> (
        CreateCellularControllerProfileParcelForTransport1PostResponse
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
        client.v1.feature_profile.sd_routing.transport.cellular_controller.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}
----------------------------------------------------------------------------------------------------------------------------


Update a Cellular Controller Profile Feature for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        cellular_controller_id: str,
        payload: EditCellularControllerProfileParcelForTransport1PutRequest,
    ) -> EditCellularControllerProfileParcelForTransport1PutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.cellular_controller.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}
-------------------------------------------------------------------------------------------------------------------------------


Delete a Cellular Controller Profile Feature for Transport feature profile

.. code:: python

    def delete(
        transport_id: str, cellular_controller_id: str
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
        client.v1.feature_profile.sd_routing.transport.cellular_controller.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller
-----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdRoutingTransportCellularControllerPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.cellular_controller.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}
----------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, cellular_controller_id: str
    ) -> GetSingleSdRoutingTransportCellularControllerPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.cellular_controller.get()


.. toctree::
    :maxdepth: 1

    cellular_profile/index
    gps/index
    models

