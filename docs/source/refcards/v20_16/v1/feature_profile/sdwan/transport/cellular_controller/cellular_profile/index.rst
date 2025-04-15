=======================================================================
v1.feature_profile.sdwan.transport.cellular_controller.cellular_profile
=======================================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile
-----------------------------------------------------------------------------------------------------------------------------------------


Associate a cellularcontroller parcel with a cellularprofile Parcel for transport feature profile

.. code:: python

    def post(
        transport_id: str,
        cellular_controller_id: str,
        payload: CreateCellularControllerAndCellularProfileParcelAssociationForTransportPostRequest,
    ) -> CreateCellularControllerAndCellularProfileParcelAssociationForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.cellular_controller.cellular_profile.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile/{cellularProfileId}
------------------------------------------------------------------------------------------------------------------------------------------------------------


Update a CellularController parcel and a CellularProfile Parcel association for transport feature profile

.. code:: python

    def put(
        transport_id: str,
        cellular_controller_id: str,
        cellular_profile_id: str,
        payload: EditCellularControllerAndCellularProfileParcelAssociationForTransportPutRequest,
    ) -> EditCellularControllerAndCellularProfileParcelAssociationForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.cellular_controller.cellular_profile.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile/{cellularProfileId}
---------------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a CellularController parcel and a CellularProfile Parcel association for transport feature profile

.. code:: python

    def delete(
        transport_id: str,
        cellular_controller_id: str,
        cellular_profile_id: str,
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
        client.v1.feature_profile.sdwan.transport.cellular_controller.cellular_profile.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile
----------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, cellular_controller_id: str
    ) -> List[
        GetCellularControllerAssociatedCellularProfileParcelsForTransportGetResponse
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
        client.v1.feature_profile.sdwan.transport.cellular_controller.cellular_profile.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile/{cellularProfileId}
------------------------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
        cellular_controller_id: str,
        cellular_profile_id: str,
    ) -> (
        GetSingleSdwanTransportCellularControllerCellularProfilePayload
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
        client.v1.feature_profile.sdwan.transport.cellular_controller.cellular_profile.get()


.. toctree::
    :maxdepth: 1

    models

