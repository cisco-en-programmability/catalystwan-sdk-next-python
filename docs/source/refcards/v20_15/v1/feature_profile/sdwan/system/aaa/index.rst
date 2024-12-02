===================================
v1.feature_profile.sdwan.system.aaa
===================================


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/aaa
--------------------------------------------------------------------------


Get Aaa Profile Parcels for System feature profile

.. code:: python

    def get_aaa_profile_parcel_for_system(system_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.system.aaa.get_aaa_profile_parcel_for_system()


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/aaa
---------------------------------------------------------------------------


Create a Aaa Profile Parcel for System feature profile

.. code:: python

    def create_aaa_profile_parcel_for_system(
        system_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.system.aaa.create_aaa_profile_parcel_for_system()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/aaa/{aaaId}
----------------------------------------------------------------------------------


Get Aaa Profile Parcel by parcelId for System feature profile

.. code:: python

    def get_aaa_profile_parcel_by_parcel_id_for_system(
        system_id: str, aaa_id: str
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
        client.v1.feature_profile.sdwan.system.aaa.get_aaa_profile_parcel_by_parcel_id_for_system()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/aaa/{aaaId}
----------------------------------------------------------------------------------


Update a Aaa Profile Parcel for System feature profile

.. code:: python

    def edit_aaa_profile_parcel_for_system(
        system_id: str, aaa_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.system.aaa.edit_aaa_profile_parcel_for_system()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/aaa/{aaaId}
-------------------------------------------------------------------------------------


Delete a Aaa Profile Parcel for System feature profile

.. code:: python

    def delete_aaa_profile_parcel_for_system(
        system_id: str, aaa_id: str
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
        client.v1.feature_profile.sdwan.system.aaa.delete_aaa_profile_parcel_for_system()


.. toctree::
    :maxdepth: 1

    schema/index

