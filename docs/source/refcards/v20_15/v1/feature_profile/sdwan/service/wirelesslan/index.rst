============================================
v1.feature_profile.sdwan.service.wirelesslan
============================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/wirelesslan
------------------------------------------------------------------------------------


Get Wirelesslan Profile Parcels for Service feature profile

.. code:: python

    def get_wirelesslan_profile_parcel_for_service(
        service_id: str,
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
        client.v1.feature_profile.sdwan.service.wirelesslan.get_wirelesslan_profile_parcel_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/wirelesslan
-------------------------------------------------------------------------------------


Create a Wirelesslan Profile Parcel for Service feature profile

.. code:: python

    def create_wirelesslan_profile_parcel_for_service(
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
        client.v1.feature_profile.sdwan.service.wirelesslan.create_wirelesslan_profile_parcel_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/wirelesslan/{wirelesslanId}
----------------------------------------------------------------------------------------------------


Get Wirelesslan Profile Parcel by parcelId for Service feature profile

.. code:: python

    def get_wirelesslan_profile_parcel_by_parcel_id_for_service(
        service_id: str, wirelesslan_id: str
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
        client.v1.feature_profile.sdwan.service.wirelesslan.get_wirelesslan_profile_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/wirelesslan/{wirelesslanId}
----------------------------------------------------------------------------------------------------


Update a Wirelesslan Profile Parcel for Service feature profile

.. code:: python

    def edit_wirelesslan_profile_parcel_for_service(
        service_id: str,
        wirelesslan_id: str,
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
        client.v1.feature_profile.sdwan.service.wirelesslan.edit_wirelesslan_profile_parcel_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/wirelesslan/{wirelesslanId}
-------------------------------------------------------------------------------------------------------


Delete a Wirelesslan Profile Parcel for Service feature profile

.. code:: python

    def delete_wirelesslan_profile_parcel_for_service(
        service_id: str, wirelesslan_id: str
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
        client.v1.feature_profile.sdwan.service.wirelesslan.delete_wirelesslan_profile_parcel_for_service()


.. toctree::
    :maxdepth: 1

    schema/index

