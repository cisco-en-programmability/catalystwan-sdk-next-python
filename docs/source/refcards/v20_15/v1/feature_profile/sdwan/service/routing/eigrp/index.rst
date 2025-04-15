==============================================
v1.feature_profile.sdwan.service.routing.eigrp
==============================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp
---------------------------------------------------------------------------------------


Create a Routing Eigrp Profile Feature for Service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateRoutingEigrpProfileParcelForServicePostRequest,
    ) -> CreateRoutingEigrpProfileParcelForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.routing.eigrp.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp/{eigrpId}
------------------------------------------------------------------------------------------------


Update a Routing Eigrp Profile Feature for Service feature profile

.. code:: python

    def put(
        service_id: str,
        eigrp_id: str,
        payload: EditRoutingEigrpProfileParcelForServicePutRequest,
    ) -> EditRoutingEigrpProfileParcelForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.routing.eigrp.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp/{eigrpId}
---------------------------------------------------------------------------------------------------


Delete a Routing Eigrp Profile Feature for Service feature profile

.. code:: python

    def delete(service_id: str, eigrp_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.routing.eigrp.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp
--------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str,
    ) -> GetListSdwanServiceRoutingEigrpPayload: ...


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
        client.v1.feature_profile.sdwan.service.routing.eigrp.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/eigrp/{eigrpId}
------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, eigrp_id: str
    ) -> GetSingleSdwanServiceRoutingEigrpPayload: ...


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
        client.v1.feature_profile.sdwan.service.routing.eigrp.get()


.. toctree::
    :maxdepth: 1

    models

