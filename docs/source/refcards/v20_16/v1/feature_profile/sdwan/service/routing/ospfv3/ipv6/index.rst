====================================================
v1.feature_profile.sdwan.service.routing.ospfv3.ipv6
====================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv6
---------------------------------------------------------------------------------------------


Create a Routing OSPFv3 IPv6 Address Family Profile Parcel for Service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateRoutingOspfv3Ipv6AfProfileParcelForServicePostRequest,
    ) -> CreateRoutingOspfv3Ipv6AfProfileParcelForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.routing.ospfv3.ipv6.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv6/{ospfv3Id}
-------------------------------------------------------------------------------------------------------


Update a Routing OSPFv3 IPv6 Address Family Profile Parcel for Service feature profile

.. code:: python

    def put(
        service_id: str,
        ospfv3_id: str,
        payload: EditRoutingOspfv3IPv6AfProfileParcelForServicePutRequest,
    ) -> EditRoutingOspfv3IPv6AfProfileParcelForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.routing.ospfv3.ipv6.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv6/{ospfv3Id}
----------------------------------------------------------------------------------------------------------


Delete a Routing OSPFv3 IPv6 Address Family Profile Parcel for Service feature profile

.. code:: python

    def delete(service_id: str, ospfv3_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.routing.ospfv3.ipv6.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv6
--------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
    ) -> GetListSdwanServiceRoutingOspfv3Ipv6Payload: ...


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
        client.v1.feature_profile.sdwan.service.routing.ospfv3.ipv6.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospfv3/ipv6/{ospfv3Id}
-------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, ospfv3_id: str
    ) -> GetSingleSdwanServiceRoutingOspfv3Ipv6Payload: ...


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
        client.v1.feature_profile.sdwan.service.routing.ospfv3.ipv6.get()


.. toctree::
    :maxdepth: 1

    models

