===================================
v1.feature_profile.sdwan.system.mrf
===================================


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/mrf
---------------------------------------------------------------------------


Create a Mrf Profile Parcel for System feature profile

.. code:: python

    def post(
        system_id: str,
        payload: CreateMrfProfileParcelForSystemPostRequest,
    ) -> CreateMrfProfileParcelForSystemPostResponse: ...


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
        client.v1.feature_profile.sdwan.system.mrf.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/mrf/{mrfId}
----------------------------------------------------------------------------------


Update a Mrf Profile Parcel for System feature profile

.. code:: python

    def put(
        system_id: str,
        mrf_id: str,
        payload: EditMrfProfileParcelForSystemPutRequest,
    ) -> EditMrfProfileParcelForSystemPutResponse: ...


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
        client.v1.feature_profile.sdwan.system.mrf.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/mrf/{mrfId}
-------------------------------------------------------------------------------------


Delete a Mrf Profile Parcel for System feature profile

.. code:: python

    def delete(system_id: str, mrf_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.system.mrf.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/mrf
--------------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetListSdwanSystemMrfPayload: ...


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
        client.v1.feature_profile.sdwan.system.mrf.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/mrf/{mrfId}
----------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, mrf_id: str
    ) -> GetSingleSdwanSystemMrfPayload: ...


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
        client.v1.feature_profile.sdwan.system.mrf.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

