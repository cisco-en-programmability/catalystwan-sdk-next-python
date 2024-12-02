===================================
v1.feature_profile.sdwan.system.mrf
===================================


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/mrf
--------------------------------------------------------------------------


Get Mrf Profile Parcels for System feature profile

.. code:: python

    def get_mrf_profile_parcel_for_system(system_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.system.mrf.get_mrf_profile_parcel_for_system()


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/mrf
---------------------------------------------------------------------------


Create a Mrf Profile Parcel for System feature profile

.. code:: python

    def create_mrf_profile_parcel_for_system(
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
        client.v1.feature_profile.sdwan.system.mrf.create_mrf_profile_parcel_for_system()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/mrf/{mrfId}
----------------------------------------------------------------------------------


Get Mrf Profile Parcel by parcelId for System feature profile

.. code:: python

    def get_mrf_profile_parcel_by_parcel_id_for_system(
        system_id: str, mrf_id: str
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
        client.v1.feature_profile.sdwan.system.mrf.get_mrf_profile_parcel_by_parcel_id_for_system()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/mrf/{mrfId}
----------------------------------------------------------------------------------


Update a Mrf Profile Parcel for System feature profile

.. code:: python

    def edit_mrf_profile_parcel_for_system(
        system_id: str, mrf_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.system.mrf.edit_mrf_profile_parcel_for_system()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/mrf/{mrfId}
-------------------------------------------------------------------------------------


Delete a Mrf Profile Parcel for System feature profile

.. code:: python

    def delete_mrf_profile_parcel_for_system(
        system_id: str, mrf_id: str
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
        client.v1.feature_profile.sdwan.system.mrf.delete_mrf_profile_parcel_for_system()


.. toctree::
    :maxdepth: 1

    schema/index

