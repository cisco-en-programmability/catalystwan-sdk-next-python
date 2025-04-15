=======================================
v1.feature_profile.sdwan.service.appqoe
=======================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/appqoe
--------------------------------------------------------------------------------


Create a Appqoe Profile Parcel for Service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateAppqoeProfileParcelForServicePostRequest,
    ) -> CreateAppqoeProfileParcelForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.appqoe.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/appqoe/{appqoeId}
------------------------------------------------------------------------------------------


Update a Appqoe Profile Parcel for Service feature profile

.. code:: python

    def put(
        service_id: str,
        appqoe_id: str,
        payload: EditAppqoeProfileParcelForServicePutRequest,
    ) -> EditAppqoeProfileParcelForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.appqoe.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/appqoe/{appqoeId}
---------------------------------------------------------------------------------------------


Delete a Appqoe Profile Parcel for Service feature profile

.. code:: python

    def delete(service_id: str, appqoe_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.appqoe.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/appqoe
-------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(service_id: str) -> GetListSdwanServiceAppqoePayload: ...


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
        client.v1.feature_profile.sdwan.service.appqoe.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/appqoe/{appqoeId}
------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, appqoe_id: str
    ) -> GetSingleSdwanServiceAppqoePayload: ...


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
        client.v1.feature_profile.sdwan.service.appqoe.get()


.. toctree::
    :maxdepth: 1

    models

