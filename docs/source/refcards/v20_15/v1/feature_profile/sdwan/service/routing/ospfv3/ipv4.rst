====================================================
v1.feature_profile.sdwan.service.routing.ospfv3.ipv4
====================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv4
--------------------------------------------------------------------------------------------


Get Routing OSPFv3 IPv4 Address Family Profile Parcels for Service feature profile

.. code:: python

    def get_routing_ospfv3_ipv4_af_profile_parcel_for_service(
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
        client.v1.feature_profile.sdwan.service.routing.ospfv3.ipv4.get_routing_ospfv3_ipv4_af_profile_parcel_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv4
---------------------------------------------------------------------------------------------


Create a Routing OSPFv3 IPv4 Address Family Profile Parcel for Service feature profile

.. code:: python

    def create_routing_ospfv3_ipv4_af_profile_parcel_for_service(
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
        client.v1.feature_profile.sdwan.service.routing.ospfv3.ipv4.create_routing_ospfv3_ipv4_af_profile_parcel_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv4/{ospfv3Id}
-------------------------------------------------------------------------------------------------------


Get Routing OSPFv3 IPv4 Address Family Profile Parcel by parcelId for Service feature profile

.. code:: python

    def get_routing_ospfv3_i_pv4_af_profile_parcel_by_parcel_id_for_service(
        service_id: str, ospfv3_id: str
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
        client.v1.feature_profile.sdwan.service.routing.ospfv3.ipv4.get_routing_ospfv3_i_pv4_af_profile_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv4/{ospfv3Id}
-------------------------------------------------------------------------------------------------------


Update a Routing OSPFv3 IPv4 Address Family Profile Parcel for Service feature profile

.. code:: python

    def edit_routing_ospfv3_i_pv4_af_profile_parcel_for_service(
        service_id: str, ospfv3_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.service.routing.ospfv3.ipv4.edit_routing_ospfv3_i_pv4_af_profile_parcel_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv4/{ospfv3Id}
----------------------------------------------------------------------------------------------------------


Delete a Routing OSPFv3 IPv4 Address Family Profile Parcel for Service feature profile

.. code:: python

    def delete_routing_ospfv3_i_pv4_af_profile_parcel_for_service(
        service_id: str, ospfv3_id: str
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
        client.v1.feature_profile.sdwan.service.routing.ospfv3.ipv4.delete_routing_ospfv3_i_pv4_af_profile_parcel_for_service()


