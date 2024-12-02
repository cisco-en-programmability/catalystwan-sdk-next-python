===================================
v1.feature_profile.sdwan.system.omp
===================================


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/omp
--------------------------------------------------------------------------


Get Omp Profile Parcels for System feature profile

.. code:: python

    def get_omp_profile_parcel_for_system(system_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.system.omp.get_omp_profile_parcel_for_system()


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/omp
---------------------------------------------------------------------------


Create a Omp Profile Parcel for System feature profile

.. code:: python

    def create_omp_profile_parcel_for_system(
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
        client.v1.feature_profile.sdwan.system.omp.create_omp_profile_parcel_for_system()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/omp/{ompId}
----------------------------------------------------------------------------------


Get Omp Profile Parcel by parcelId for System feature profile

.. code:: python

    def get_omp_profile_parcel_by_parcel_id_for_system(
        system_id: str, omp_id: str
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
        client.v1.feature_profile.sdwan.system.omp.get_omp_profile_parcel_by_parcel_id_for_system()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/omp/{ompId}
----------------------------------------------------------------------------------


Update a Omp Profile Parcel for System feature profile

.. code:: python

    def edit_omp_profile_parcel_for_system(
        system_id: str, omp_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.system.omp.edit_omp_profile_parcel_for_system()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/omp/{ompId}
-------------------------------------------------------------------------------------


Delete a Omp Profile Parcel for System feature profile

.. code:: python

    def delete_omp_profile_parcel_for_system(
        system_id: str, omp_id: str
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
        client.v1.feature_profile.sdwan.system.omp.delete_omp_profile_parcel_for_system()


.. toctree::
    :maxdepth: 1

    schema/index

