===========================================
v1.feature_profile.sdwan.service.switchport
===========================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/switchport
-----------------------------------------------------------------------------------


Get Switchport Parcels for service feature profile

.. code:: python

    def get_switchport_parcels_for_service(service_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.service.switchport.get_switchport_parcels_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/switchport
------------------------------------------------------------------------------------


Create a switchport Parcel to a service feature profile

.. code:: python

    def cedge_service_profile_switchport_parcel_restful_resource(
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
        client.v1.feature_profile.sdwan.service.switchport.cedge_service_profile_switchport_parcel_restful_resource()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/switchport/{switchportId}
--------------------------------------------------------------------------------------------------


Get Switchport Parcel by switchportId for service feature profile

.. code:: python

    def get_switchport_parcel_by_parcel_id_for_service(
        service_id: str, switchport_id: str
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
        client.v1.feature_profile.sdwan.service.switchport.get_switchport_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/switchport/{switchportId}
--------------------------------------------------------------------------------------------------


Update a Switchport Parcel association for service feature profile

.. code:: python

    def edit_switchport_parcel_association_for_service(
        service_id: str, switchport_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.service.switchport.edit_switchport_parcel_association_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/switchport/{switchportId}
-----------------------------------------------------------------------------------------------------


Delete a Switchport Parcel for service feature profile

.. code:: python

    def delete_switchport_profile_parcel_for_service(
        service_id: str, switchport_id: str
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
        client.v1.feature_profile.sdwan.service.switchport.delete_switchport_profile_parcel_for_service()


.. toctree::
    :maxdepth: 1

    schema/index

