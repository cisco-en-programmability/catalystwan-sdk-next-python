=============================================
v1.feature_profile.sdwan.service.routing.ospf
=============================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospf
--------------------------------------------------------------------------------------


Create a Routing Ospf Profile Parcel for Service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateRoutingOspfProfileParcelForServicePostRequest,
    ) -> CreateRoutingOspfProfileParcelForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.routing.ospf.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospf/{ospfId}
----------------------------------------------------------------------------------------------


Update a Routing Ospf Profile Parcel for Service feature profile

.. code:: python

    def put(
        service_id: str,
        ospf_id: str,
        payload: EditRoutingOspfProfileParcelForServicePutRequest,
    ) -> EditRoutingOspfProfileParcelForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.routing.ospf.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospf/{ospfId}
-------------------------------------------------------------------------------------------------


Delete a Routing Ospf Profile Parcel for Service feature profile

.. code:: python

    def delete(service_id: str, ospf_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.routing.ospf.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospf
-------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(service_id: str) -> GetListSdwanServiceRoutingOspfPayload: ...


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
        client.v1.feature_profile.sdwan.service.routing.ospf.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/routing/ospf/{ospfId}
----------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, ospf_id: str
    ) -> GetSingleSdwanServiceRoutingOspfPayload: ...


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
        client.v1.feature_profile.sdwan.service.routing.ospf.get()


.. toctree::
    :maxdepth: 1

    models

