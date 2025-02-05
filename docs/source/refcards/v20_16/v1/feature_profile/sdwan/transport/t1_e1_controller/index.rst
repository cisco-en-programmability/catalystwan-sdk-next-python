===================================================
v1.feature_profile.sdwan.transport.t1_e1_controller
===================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/t1-e1-controller
---------------------------------------------------------------------------------------------


Get T1e1controller Profile Parcels for Transport feature profile

.. code:: python

    def get_t1e1controller_profile_parcel_for_transport(
        transport_id: str,
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
        client.v1.feature_profile.sdwan.transport.t1_e1_controller.get_t1e1controller_profile_parcel_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/t1-e1-controller
----------------------------------------------------------------------------------------------


Create a T1e1controller Profile Parcel for Transport feature profile

.. code:: python

    def create_t1e1controller_profile_parcel_for_transport(
        transport_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.transport.t1_e1_controller.create_t1e1controller_profile_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/t1-e1-controller/{t1e1controllerId}
----------------------------------------------------------------------------------------------------------------


Get T1e1controller Profile Parcel by parcelId for Transport feature profile

.. code:: python

    def get_t1e1controller_profile_parcel_by_parcel_id_for_transport(
        transport_id: str, t1e1controller_id: str
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
        client.v1.feature_profile.sdwan.transport.t1_e1_controller.get_t1e1controller_profile_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/t1-e1-controller/{t1e1controllerId}
----------------------------------------------------------------------------------------------------------------


Update a T1e1controller Profile Parcel for Transport feature profile

.. code:: python

    def edit_t1e1controller_profile_parcel_for_transport(
        transport_id: str,
        t1e1controller_id: str,
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
        client.v1.feature_profile.sdwan.transport.t1_e1_controller.edit_t1e1controller_profile_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/t1-e1-controller/{t1e1controllerId}
-------------------------------------------------------------------------------------------------------------------


Delete a T1e1controller Profile Parcel for Transport feature profile

.. code:: python

    def delete_t1e1controller_profile_parcel_for_transport(
        transport_id: str, t1e1controller_id: str
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
        client.v1.feature_profile.sdwan.transport.t1_e1_controller.delete_t1e1controller_profile_parcel_for_transport()


.. toctree::
    :maxdepth: 1

    schema/index

