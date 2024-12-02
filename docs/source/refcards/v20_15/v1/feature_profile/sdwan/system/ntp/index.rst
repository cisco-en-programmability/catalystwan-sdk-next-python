===================================
v1.feature_profile.sdwan.system.ntp
===================================


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/ntp
--------------------------------------------------------------------------


Get Ntp Profile Parcels for System feature profile

.. code:: python

    def get_ntp_profile_parcel_for_system(system_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.system.ntp.get_ntp_profile_parcel_for_system()


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/ntp
---------------------------------------------------------------------------


Create a Ntp Profile Parcel for System feature profile

.. code:: python

    def create_ntp_profile_parcel_for_system(
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
        client.v1.feature_profile.sdwan.system.ntp.create_ntp_profile_parcel_for_system()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/ntp/{ntpId}
----------------------------------------------------------------------------------


Get Ntp Profile Parcel by parcelId for System feature profile

.. code:: python

    def get_ntp_profile_parcel_by_parcel_id_for_system(
        system_id: str, ntp_id: str
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
        client.v1.feature_profile.sdwan.system.ntp.get_ntp_profile_parcel_by_parcel_id_for_system()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/ntp/{ntpId}
----------------------------------------------------------------------------------


Update a Ntp Profile Parcel for System feature profile

.. code:: python

    def edit_ntp_profile_parcel_for_system(
        system_id: str, ntp_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.system.ntp.edit_ntp_profile_parcel_for_system()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/ntp/{ntpId}
-------------------------------------------------------------------------------------


Delete a Ntp Profile Parcel for System feature profile

.. code:: python

    def delete_ntp_profile_parcel_for_system(
        system_id: str, ntp_id: str
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
        client.v1.feature_profile.sdwan.system.ntp.delete_ntp_profile_parcel_for_system()


.. toctree::
    :maxdepth: 1

    schema/index

