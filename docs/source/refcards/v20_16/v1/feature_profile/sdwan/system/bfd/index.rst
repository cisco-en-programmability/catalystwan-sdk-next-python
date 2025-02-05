===================================
v1.feature_profile.sdwan.system.bfd
===================================


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/bfd
--------------------------------------------------------------------------


Get Bfd Profile Parcels for System feature profile

.. code:: python

    def get_bfd_profile_parcel_for_system(system_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.system.bfd.get_bfd_profile_parcel_for_system()


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/bfd
---------------------------------------------------------------------------


Create a Bfd Profile Parcel for System feature profile

.. code:: python

    def create_bfd_profile_parcel_for_system(
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
        client.v1.feature_profile.sdwan.system.bfd.create_bfd_profile_parcel_for_system()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/bfd/{bfdId}
----------------------------------------------------------------------------------


Get Bfd Profile Parcel by parcelId for System feature profile

.. code:: python

    def get_bfd_profile_parcel_by_parcel_id_for_system(
        system_id: str, bfd_id: str
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
        client.v1.feature_profile.sdwan.system.bfd.get_bfd_profile_parcel_by_parcel_id_for_system()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/bfd/{bfdId}
----------------------------------------------------------------------------------


Update a Bfd Profile Parcel for System feature profile

.. code:: python

    def edit_bfd_profile_parcel_for_system(
        system_id: str, bfd_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.system.bfd.edit_bfd_profile_parcel_for_system()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/bfd/{bfdId}
-------------------------------------------------------------------------------------


Delete a Bfd Profile Parcel for System feature profile

.. code:: python

    def delete_bfd_profile_parcel_for_system(
        system_id: str, bfd_id: str
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
        client.v1.feature_profile.sdwan.system.bfd.delete_bfd_profile_parcel_for_system()


.. toctree::
    :maxdepth: 1

    schema/index

