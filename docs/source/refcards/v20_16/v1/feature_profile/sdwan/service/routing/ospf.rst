=============================================
v1.feature_profile.sdwan.service.routing.ospf
=============================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospf
-------------------------------------------------------------------------------------


Get Routing Ospf Profile Parcels for Service feature profile

.. code:: python

    def get_routing_ospf_profile_parcel_for_service(
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
        client.v1.feature_profile.sdwan.service.routing.ospf.get_routing_ospf_profile_parcel_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospf
--------------------------------------------------------------------------------------


Create a Routing Ospf Profile Parcel for Service feature profile

.. code:: python

    def create_routing_ospf_profile_parcel_for_service(
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
        client.v1.feature_profile.sdwan.service.routing.ospf.create_routing_ospf_profile_parcel_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospf/{ospfId}
----------------------------------------------------------------------------------------------


Get Routing Ospf Profile Parcel by parcelId for Service feature profile

.. code:: python

    def get_routing_ospf_profile_parcel_by_parcel_id_for_service(
        service_id: str, ospf_id: str
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
        client.v1.feature_profile.sdwan.service.routing.ospf.get_routing_ospf_profile_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospf/{ospfId}
----------------------------------------------------------------------------------------------


Update a Routing Ospf Profile Parcel for Service feature profile

.. code:: python

    def edit_routing_ospf_profile_parcel_for_service(
        service_id: str, ospf_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.service.routing.ospf.edit_routing_ospf_profile_parcel_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospf/{ospfId}
-------------------------------------------------------------------------------------------------


Delete a Routing Ospf Profile Parcel for Service feature profile

.. code:: python

    def delete_routing_ospf_profile_parcel_for_service(
        service_id: str, ospf_id: str
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
        client.v1.feature_profile.sdwan.service.routing.ospf.delete_routing_ospf_profile_parcel_for_service()


