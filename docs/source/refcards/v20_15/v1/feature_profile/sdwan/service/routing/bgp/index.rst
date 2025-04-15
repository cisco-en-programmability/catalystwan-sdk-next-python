============================================
v1.feature_profile.sdwan.service.routing.bgp
============================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/bgp
-------------------------------------------------------------------------------------


Create a Routing Bgp Profile Parcel for Service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateRoutingBgpProfileParcelForServicePostRequest,
    ) -> CreateRoutingBgpProfileParcelForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.routing.bgp.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/bgp/{bgpId}
--------------------------------------------------------------------------------------------


Update a Routing Bgp Profile Parcel for Service feature profile

.. code:: python

    def put(
        service_id: str,
        bgp_id: str,
        payload: EditRoutingBgpProfileParcelForServicePutRequest,
    ) -> EditRoutingBgpProfileParcelForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.routing.bgp.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/bgp/{bgpId}
-----------------------------------------------------------------------------------------------


Delete a Routing Bgp Profile Parcel for Service feature profile

.. code:: python

    def delete(service_id: str, bgp_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.routing.bgp.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/bgp
------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(service_id: str) -> GetListSdwanServiceRoutingBgpPayload: ...


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
        client.v1.feature_profile.sdwan.service.routing.bgp.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/bgp/{bgpId}
--------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, bgp_id: str
    ) -> GetSingleSdwanServiceRoutingBgpPayload: ...


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
        client.v1.feature_profile.sdwan.service.routing.bgp.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

