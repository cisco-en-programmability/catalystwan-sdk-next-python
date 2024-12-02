=======================================
v1.feature_profile.sdwan.service.appqoe
=======================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/appqoe
-------------------------------------------------------------------------------


Get Appqoe Profile Parcels for Service feature profile

.. code:: python

    def get_appqoe_profile_parcel_for_service(service_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.service.appqoe.get_appqoe_profile_parcel_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/appqoe
--------------------------------------------------------------------------------


Create a Appqoe Profile Parcel for Service feature profile

.. code:: python

    def create_appqoe_profile_parcel_for_service(
        service_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.service.appqoe.create_appqoe_profile_parcel_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/appqoe/{appqoeId}
------------------------------------------------------------------------------------------


Get Appqoe Profile Parcel by parcelId for Service feature profile

.. code:: python

    def get_appqoe_profile_parcel_by_parcel_id_for_service(
        service_id: str, appqoe_id: str
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
        client.v1.feature_profile.sdwan.service.appqoe.get_appqoe_profile_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/appqoe/{appqoeId}
------------------------------------------------------------------------------------------


Update a Appqoe Profile Parcel for Service feature profile

.. code:: python

    def edit_appqoe_profile_parcel_for_service(
        service_id: str, appqoe_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.service.appqoe.edit_appqoe_profile_parcel_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/appqoe/{appqoeId}
---------------------------------------------------------------------------------------------


Delete a Appqoe Profile Parcel for Service feature profile

.. code:: python

    def delete_appqoe_profile_parcel_for_service(
        service_id: str, appqoe_id: str
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
        client.v1.feature_profile.sdwan.service.appqoe.delete_appqoe_profile_parcel_for_service()


