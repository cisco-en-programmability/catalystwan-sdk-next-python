==================================================
v1.feature_profile.sdwan.service.routing.multicast
==================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/multicast
-------------------------------------------------------------------------------------------


Create a Routing Multicast Profile Parcel for Service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateRoutingMulticastProfileParcelForServicePostRequest,
    ) -> CreateRoutingMulticastProfileParcelForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.routing.multicast.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/multicast/{multicastId}
--------------------------------------------------------------------------------------------------------


Update a Routing Multicast Profile Parcel for Service feature profile

.. code:: python

    def put(
        service_id: str,
        multicast_id: str,
        payload: EditRoutingMulticastProfileParcelForServicePutRequest,
    ) -> EditRoutingMulticastProfileParcelForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.routing.multicast.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/multicast/{multicastId}
-----------------------------------------------------------------------------------------------------------


Delete a Routing Multicast Profile Parcel for Service feature profile

.. code:: python

    def delete(service_id: str, multicast_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.routing.multicast.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/multicast
------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
    ) -> GetListSdwanServiceRoutingMulticastPayload: ...


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
        client.v1.feature_profile.sdwan.service.routing.multicast.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/multicast/{multicastId}
--------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, multicast_id: str
    ) -> GetSingleSdwanServiceRoutingMulticastPayload: ...


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
        client.v1.feature_profile.sdwan.service.routing.multicast.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

