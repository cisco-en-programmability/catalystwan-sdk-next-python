===============================================
v1.feature_profile.sdwan.transport.routing.ospf
===============================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospf
------------------------------------------------------------------------------------------


Create a Routing Ospf Profile Parcel for Transport feature profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateRoutingOspfProfileParcelForTransportPostRequest,
    ) -> CreateRoutingOspfProfileParcelForTransportPostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.routing.ospf.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospf/{ospfId}
--------------------------------------------------------------------------------------------------


Update a Routing Ospf Profile Parcel for Transport feature profile

.. code:: python

    def put(
        transport_id: str,
        ospf_id: str,
        payload: EditRoutingOspfProfileParcelForTransportPutRequest,
    ) -> EditRoutingOspfProfileParcelForTransportPutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.routing.ospf.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospf/{ospfId}
-----------------------------------------------------------------------------------------------------


Delete a Routing Ospf Profile Parcel for Transport feature profile

.. code:: python

    def delete(transport_id: str, ospf_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.routing.ospf.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospf
-----------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdwanTransportRoutingOspfPayload: ...


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
        client.v1.feature_profile.sdwan.transport.routing.ospf.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/routing/ospf/{ospfId}
--------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, ospf_id: str
    ) -> GetSingleSdwanTransportRoutingOspfPayload: ...


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
        client.v1.feature_profile.sdwan.transport.routing.ospf.get()


.. toctree::
    :maxdepth: 1

    models

