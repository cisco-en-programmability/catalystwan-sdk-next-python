=======================================
v1.feature_profile.sdwan.system.global_
=======================================


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/global
-----------------------------------------------------------------------------


Get Global Profile Parcels for System feature profile

.. code:: python

    def get_global_profile_parcel_for_system(system_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.system.global_.get_global_profile_parcel_for_system()


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/global
------------------------------------------------------------------------------


Create a Global Profile Parcel for System feature profile

.. code:: python

    def create_global_profile_parcel_for_system(
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
        client.v1.feature_profile.sdwan.system.global_.create_global_profile_parcel_for_system()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/global/{globalId}
----------------------------------------------------------------------------------------


Get Global Profile Parcel by parcelId for System feature profile

.. code:: python

    def get_global_profile_parcel_by_parcel_id_for_system(
        system_id: str, global_id: str
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
        client.v1.feature_profile.sdwan.system.global_.get_global_profile_parcel_by_parcel_id_for_system()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/global/{globalId}
----------------------------------------------------------------------------------------


Update a Global Profile Parcel for System feature profile

.. code:: python

    def edit_global_profile_parcel_for_system(
        system_id: str, global_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.system.global_.edit_global_profile_parcel_for_system()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/global/{globalId}
-------------------------------------------------------------------------------------------


Delete a Global Profile Parcel for System feature profile

.. code:: python

    def delete_global_profile_parcel_for_system(
        system_id: str, global_id: str
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
        client.v1.feature_profile.sdwan.system.global_.delete_global_profile_parcel_for_system()


.. toctree::
    :maxdepth: 1

    schema/index

