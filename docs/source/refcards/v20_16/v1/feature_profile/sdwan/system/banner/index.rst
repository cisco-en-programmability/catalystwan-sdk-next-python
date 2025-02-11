======================================
v1.feature_profile.sdwan.system.banner
======================================


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/banner
-----------------------------------------------------------------------------


Get Banner Profile Parcels for System feature profile

.. code:: python

    def get_banner_profile_parcel_for_system(system_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.system.banner.get_banner_profile_parcel_for_system()


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/banner
------------------------------------------------------------------------------


Create a Banner Profile Parcel for System feature profile

.. code:: python

    def create_banner_profile_parcel_for_system(
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
        client.v1.feature_profile.sdwan.system.banner.create_banner_profile_parcel_for_system()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/banner/{bannerId}
----------------------------------------------------------------------------------------


Get Banner Profile Parcel by parcelId for System feature profile

.. code:: python

    def get_banner_profile_parcel_by_parcel_id_for_system(
        system_id: str, banner_id: str
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
        client.v1.feature_profile.sdwan.system.banner.get_banner_profile_parcel_by_parcel_id_for_system()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/banner/{bannerId}
----------------------------------------------------------------------------------------


Update a Banner Profile Parcel for System feature profile

.. code:: python

    def edit_banner_profile_parcel_for_system(
        system_id: str, banner_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.system.banner.edit_banner_profile_parcel_for_system()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/banner/{bannerId}
-------------------------------------------------------------------------------------------


Delete a Banner Profile Parcel for System feature profile

.. code:: python

    def delete_banner_profile_parcel_for_system(
        system_id: str, banner_id: str
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
        client.v1.feature_profile.sdwan.system.banner.delete_banner_profile_parcel_for_system()


.. toctree::
    :maxdepth: 1

    schema/index

