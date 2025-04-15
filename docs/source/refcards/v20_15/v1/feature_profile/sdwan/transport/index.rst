==================================
v1.feature_profile.sdwan.transport
==================================


Operation: POST /dataservice/v1/feature-profile/sdwan/transport
---------------------------------------------------------------


Create a SDWAN Transport Feature Profile

.. code:: python

    def post(
        payload: CreateSdwanTransportFeatureProfilePostRequest,
    ) -> CreateSdwanTransportFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.sdwan.transport.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}
----------------------------------------------------------------------------


Edit a SDWAN Transport Feature Profile

.. code:: python

    def put(
        transport_id: str,
        payload: EditSdwanTransportFeatureProfilePutRequest,
    ) -> EditSdwanTransportFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.sdwan.transport.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}
-------------------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete(transport_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.transport.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport
--------------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> List[GetSdwanTransportFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.sdwan.transport.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}
----------------------------------------------------------------------------


.. code:: python

    @overload
    def get(transport_id: str) -> GetSingleSdwanTransportPayload: ...


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
        client.v1.feature_profile.sdwan.transport.get()


.. toctree::
    :maxdepth: 1

    cellular_controller/index
    cellular_profile/index
    ipv6_tracker/index
    ipv6_trackergroup/index
    management/index
    routing/index
    t1_e1_controller/index
    tracker/index
    trackergroup/index
    wan/index
    esimcellular_controller/index
    esimcellular_profile/index
    gps/index
    models

