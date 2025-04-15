================================
v1.feature_profile.sdwan.service
================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service
-------------------------------------------------------------


Create a SDWAN Service Feature Profile

.. code:: python

    def post(
        payload: CreateSdwanServiceFeatureProfilePostRequest,
    ) -> CreateSdwanServiceFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}
------------------------------------------------------------------------


Edit a SDWAN Service Feature Profile

.. code:: python

    def put(
        service_id: str, payload: EditSdwanServiceFeatureProfilePutRequest
    ) -> EditSdwanServiceFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}
---------------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete(service_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service
------------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        details: Optional[bool] = False,
    ) -> List[GetSdwanServiceFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.sdwan.service.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}
------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, details: Optional[bool] = False
    ) -> GetSingleSdwanServicePayload: ...


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
        client.v1.feature_profile.sdwan.service.get()


.. toctree::
    :maxdepth: 1

    dhcp_server/index
    lan/index
    routing/index
    switchport/index
    tracker/index
    trackergroup/index
    wirelesslan/index
    appqoe/index
    models

