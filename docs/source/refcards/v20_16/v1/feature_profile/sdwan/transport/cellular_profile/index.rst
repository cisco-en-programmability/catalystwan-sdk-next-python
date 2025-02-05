===================================================
v1.feature_profile.sdwan.transport.cellular_profile
===================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-profile
---------------------------------------------------------------------------------------------


Get Cellular Profile Profile Parcels for Transport feature profile

.. code:: python

    def get_cellular_profile_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.cellular_profile.get_cellular_profile_profile_parcel_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-profile
----------------------------------------------------------------------------------------------


Create a Cellular Profile Profile Parcel for Transport feature profile

.. code:: python

    def create_cellular_profile_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.cellular_profile.create_cellular_profile_profile_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-profile/{cellularProfileId}
-----------------------------------------------------------------------------------------------------------------


Get Cellular Profile Profile Parcel by parcelId for Transport feature profile

.. code:: python

    def get_cellular_profile_profile_parcel_by_parcel_id_for_transport(
        transport_id: str, cellular_profile_id: str
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
        client.v1.feature_profile.sdwan.transport.cellular_profile.get_cellular_profile_profile_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-profile/{cellularProfileId}
-----------------------------------------------------------------------------------------------------------------


Update a Cellular Profile Profile Parcel for Transport feature profile

.. code:: python

    def edit_cellular_profile_profile_parcel_for_transport(
        transport_id: str,
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
        client.v1.feature_profile.sdwan.transport.cellular_profile.edit_cellular_profile_profile_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/cellular-profile/{cellularProfileId}
--------------------------------------------------------------------------------------------------------------------


Delete a Cellular Profile Profile Parcel for Transport feature profile

.. code:: python

    def delete_cellular_profile_profile_parcel_for_transport(
        transport_id: str, cellular_profile_id: str
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
        client.v1.feature_profile.sdwan.transport.cellular_profile.delete_cellular_profile_profile_parcel_for_transport()


.. toctree::
    :maxdepth: 1

    schema/index

