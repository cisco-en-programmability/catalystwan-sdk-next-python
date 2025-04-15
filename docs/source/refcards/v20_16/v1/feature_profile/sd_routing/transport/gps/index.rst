===========================================
v1.feature_profile.sd_routing.transport.gps
===========================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/gps
--------------------------------------------------------------------------------------


Create a GPS Profile Feature for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateGpsProfileParcelForTransportPostRequest,
    ) -> CreateGpsProfileParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.gps.post()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/gps/{gpsId}
------------------------------------------------------------------------------------------------


Delete a GPS Profile Feature for Transport feature profile

.. code:: python

    def delete(transport_id: str, gps_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.transport.gps.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/gps
-------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(transport_id: str) -> GetListSdRoutingTransportGpsPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.gps.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/gps/{gpsId}
---------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, gps_id: str
    ) -> GetSingleSdRoutingTransportGpsPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.gps.get()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/gps/{gpsId}
---------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def put(
        transport_id: str,
        gps_id: str,
        payload: EditGpsProfileParcelForTransportPutRequest,
    ) -> EditGpsProfileParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.gps.put()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/{cellularControllerId}/gps/{gpsId}
--------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def put(
        transport_id: str,
        gps_id: str,
        payload: EditCellularControllerAndGpsParcelAssociationForTransport1PutRequest,
        cellular_controller_id: str,
    ) -> EditCellularControllerAndGpsParcelAssociationForTransport1PutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.gps.put()


.. toctree::
    :maxdepth: 1

    models

