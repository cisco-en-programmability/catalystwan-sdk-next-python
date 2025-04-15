===============================================================
v1.feature_profile.sd_routing.transport.cellular_controller.gps
===============================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}/gps
---------------------------------------------------------------------------------------------------------------------------------


Associate a cellularcontroller feature with a GPS Parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        cellular_controller_id: str,
        payload: CreateCellularControllerAndGpsParcelAssociationForTransport1PostRequest,
    ) -> CreateCellularControllerAndGpsParcelAssociationForTransport1PostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.cellular_controller.gps.post()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}/gps/{gpsId}
-------------------------------------------------------------------------------------------------------------------------------------------


Delete a CellularController feature and a GPS Feature association for transport feature profile

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
        client.v1.feature_profile.sd_routing.transport.cellular_controller.gps.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}/gps
--------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, cellular_controller_id: str
    ) -> List[
        GetCellularControllerAssociatedGpsParcelsForTransport1GetResponse
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
        client.v1.feature_profile.sd_routing.transport.cellular_controller.gps.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/cellular-controller/{cellularControllerId}/gps/{gpsId}
----------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, cellular_controller_id: str, gps_id: str
    ) -> GetSingleSdRoutingTransportCellularControllerGpsPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.cellular_controller.gps.get()


.. toctree::
    :maxdepth: 1

    models

