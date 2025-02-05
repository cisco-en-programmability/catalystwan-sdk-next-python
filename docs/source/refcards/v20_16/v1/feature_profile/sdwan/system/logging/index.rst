=======================================
v1.feature_profile.sdwan.system.logging
=======================================


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/logging
------------------------------------------------------------------------------


Get Logging Profile Parcels for System feature profile

.. code:: python

    def get_logging_profile_parcel_for_system(system_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.system.logging.get_logging_profile_parcel_for_system()


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/logging
-------------------------------------------------------------------------------


Create a Logging Profile Parcel for System feature profile

.. code:: python

    def create_logging_profile_parcel_for_system(
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
        client.v1.feature_profile.sdwan.system.logging.create_logging_profile_parcel_for_system()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/logging/{loggingId}
------------------------------------------------------------------------------------------


Get Logging Profile Parcel by parcelId for System feature profile

.. code:: python

    def get_logging_profile_parcel_by_parcel_id_for_system(
        system_id: str, logging_id: str
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
        client.v1.feature_profile.sdwan.system.logging.get_logging_profile_parcel_by_parcel_id_for_system()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/logging/{loggingId}
------------------------------------------------------------------------------------------


Update a Logging Profile Parcel for System feature profile

.. code:: python

    def edit_logging_profile_parcel_for_system(
        system_id: str, logging_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.system.logging.edit_logging_profile_parcel_for_system()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/logging/{loggingId}
---------------------------------------------------------------------------------------------


Delete a Logging Profile Parcel for System feature profile

.. code:: python

    def delete_logging_profile_parcel_for_system(
        system_id: str, logging_id: str
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
        client.v1.feature_profile.sdwan.system.logging.delete_logging_profile_parcel_for_system()


.. toctree::
    :maxdepth: 1

    schema/index

