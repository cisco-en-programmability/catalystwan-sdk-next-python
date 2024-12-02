=======================================================================
v1.feature_profile.sdwan.transport.cellular_controller.cellular_profile
=======================================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile
----------------------------------------------------------------------------------------------------------------------------------------


Get CellularController associated Cellular Profile Parcels for transport feature profile

.. code:: python

    def get_cellular_controller_associated_cellular_profile_parcels_for_transport(
        transport_id: str, cellular_controller_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.cellular_controller.cellular_profile.get_cellular_controller_associated_cellular_profile_parcels_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile
-----------------------------------------------------------------------------------------------------------------------------------------


Associate a cellularcontroller parcel with a cellularprofile Parcel for transport feature profile

.. code:: python

    def create_cellular_controller_and_cellular_profile_parcel_association_for_transport(
        transport_id: str,
        cellular_controller_id: str,
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.cellular_controller.cellular_profile.create_cellular_controller_and_cellular_profile_parcel_association_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile/{cellularProfileId}
------------------------------------------------------------------------------------------------------------------------------------------------------------


Get CellularController parcel associated CellularProfile Parcel by cellularProfileId for transport feature profile

.. code:: python

    def get_cellular_controller_associated_cellular_profile_parcel_by_parcel_id_for_transport(
        transport_id: str,
        cellular_controller_id: str,
        cellular_profile_id: str,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.cellular_controller.cellular_profile.get_cellular_controller_associated_cellular_profile_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile/{cellularProfileId}
------------------------------------------------------------------------------------------------------------------------------------------------------------


Update a CellularController parcel and a CellularProfile Parcel association for transport feature profile

.. code:: python

    def edit_cellular_controller_and_cellular_profile_parcel_association_for_transport(
        transport_id: str,
        cellular_controller_id: str,
        cellular_profile_id: str,
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.transport.cellular_controller.cellular_profile.edit_cellular_controller_and_cellular_profile_parcel_association_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-controller/{cellularControllerId}/cellular-profile/{cellularProfileId}
---------------------------------------------------------------------------------------------------------------------------------------------------------------


Delete a CellularController parcel and a CellularProfile Parcel association for transport feature profile

.. code:: python

    def delete_cellular_controller_and_cellular_profile_association_for_transport(
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
        client.v1.feature_profile.sdwan.transport.cellular_controller.cellular_profile.delete_cellular_controller_and_cellular_profile_association_for_transport()


