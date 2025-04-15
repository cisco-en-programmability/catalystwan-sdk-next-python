==========================================================
v1.feature_profile.sdwan.transport.cellular_controller.gps
==========================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps
----------------------------------------------------------------------------------------------------------------------------


Associate a cellularcontroller parcel with a gps Parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        cellular_controller_id: str,
        payload: CreateCellularControllerAndGpsParcelAssociationForTransportPostRequest,
    ) -> CreateCellularControllerAndGpsParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.cellular_controller.gps.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps/{gpsId}
-----------------------------------------------------------------------------------------------------------------------------------


Update a CellularController parcel and a Gps Parcel association for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        cellular_controller_id: str,
        gps_id: str,
        payload: EditCellularControllerAndGpsParcelAssociationForTransportPutRequest,
    ) -> EditCellularControllerAndGpsParcelAssociationForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.cellular_controller.gps.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps/{gpsId}
--------------------------------------------------------------------------------------------------------------------------------------


Delete a CellularController parcel and a Gps Parcel association for transport feature profile

.. code:: python

    def delete(
        transport_id: str, cellular_controller_id: str, gps_id: str
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
        client.v1.feature_profile.sdwan.transport.cellular_controller.gps.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps
---------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, cellular_controller_id: str
    ) -> List[
        GetCellularControllerAssociatedGpsParcelsForTransportGetResponse
    ]: ...


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
        client.v1.feature_profile.sdwan.transport.cellular_controller.gps.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/gps/{gpsId}
-----------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, cellular_controller_id: str, gps_id: str
    ) -> GetSingleSdwanTransportCellularControllerGpsPayload: ...


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
        client.v1.feature_profile.sdwan.transport.cellular_controller.gps.get()


.. toctree::
    :maxdepth: 1

    models

