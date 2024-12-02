==================================================
v1.feature_profile.sdwan.service.routing.multicast
==================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/multicast
------------------------------------------------------------------------------------------


Get Routing Multicast Profile Parcels for Service feature profile

.. code:: python

    def get_routing_multicast_profile_parcel_for_service(
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
        client.v1.feature_profile.sdwan.service.routing.multicast.get_routing_multicast_profile_parcel_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/multicast
-------------------------------------------------------------------------------------------


Create a Routing Multicast Profile Parcel for Service feature profile

.. code:: python

    def create_routing_multicast_profile_parcel_for_service(
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
        client.v1.feature_profile.sdwan.service.routing.multicast.create_routing_multicast_profile_parcel_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/multicast/{multicastId}
--------------------------------------------------------------------------------------------------------


Get Routing Multicast Profile Parcel by parcelId for Service feature profile

.. code:: python

    def get_routing_multicast_profile_parcel_by_parcel_id_for_service(
        service_id: str, multicast_id: str
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
        client.v1.feature_profile.sdwan.service.routing.multicast.get_routing_multicast_profile_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/multicast/{multicastId}
--------------------------------------------------------------------------------------------------------


Update a Routing Multicast Profile Parcel for Service feature profile

.. code:: python

    def edit_routing_multicast_profile_parcel_for_service(
        service_id: str, multicast_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.service.routing.multicast.edit_routing_multicast_profile_parcel_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/multicast/{multicastId}
-----------------------------------------------------------------------------------------------------------


Delete a Routing Multicast Profile Parcel for Service feature profile

.. code:: python

    def delete_routing_multicast_profile_parcel_for_service(
        service_id: str, multicast_id: str
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
        client.v1.feature_profile.sdwan.service.routing.multicast.delete_routing_multicast_profile_parcel_for_service()


.. toctree::
    :maxdepth: 1

    schema/index

