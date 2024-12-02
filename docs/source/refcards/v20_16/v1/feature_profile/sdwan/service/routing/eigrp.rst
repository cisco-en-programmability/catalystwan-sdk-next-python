==============================================
v1.feature_profile.sdwan.service.routing.eigrp
==============================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp
--------------------------------------------------------------------------------------


Get Routing Eigrp Profile Features for Service feature profile

.. code:: python

    def get_routing_eigrp_profile_parcel_for_service(
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
        client.v1.feature_profile.sdwan.service.routing.eigrp.get_routing_eigrp_profile_parcel_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp
---------------------------------------------------------------------------------------


Create a Routing Eigrp Profile Feature for Service feature profile

.. code:: python

    def create_routing_eigrp_profile_parcel_for_service(
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
        client.v1.feature_profile.sdwan.service.routing.eigrp.create_routing_eigrp_profile_parcel_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp/{eigrpId}
------------------------------------------------------------------------------------------------


Get Routing Eigrp Profile Feature by parcelId for Service feature profile

.. code:: python

    def get_routing_eigrp_profile_parcel_by_parcel_id_for_service(
        service_id: str, eigrp_id: str
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
        client.v1.feature_profile.sdwan.service.routing.eigrp.get_routing_eigrp_profile_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp/{eigrpId}
------------------------------------------------------------------------------------------------


Update a Routing Eigrp Profile Feature for Service feature profile

.. code:: python

    def edit_routing_eigrp_profile_parcel_for_service(
        service_id: str, eigrp_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.service.routing.eigrp.edit_routing_eigrp_profile_parcel_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp/{eigrpId}
---------------------------------------------------------------------------------------------------


Delete a Routing Eigrp Profile Feature for Service feature profile

.. code:: python

    def delete_routing_eigrp_profile_parcel_for_service(
        service_id: str, eigrp_id: str
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
        client.v1.feature_profile.sdwan.service.routing.eigrp.delete_routing_eigrp_profile_parcel_for_service()


