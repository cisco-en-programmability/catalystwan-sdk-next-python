===================================
v1.feature_profile.sdwan.system.omp
===================================


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/omp
---------------------------------------------------------------------------


Create a Omp Profile Parcel for System feature profile

.. code:: python

    def post(
        system_id: str,
        payload: CreateOmpProfileParcelForSystemPostRequest,
    ) -> CreateOmpProfileParcelForSystemPostResponse: ...


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
        client.v1.feature_profile.sdwan.system.omp.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/omp/{ompId}
----------------------------------------------------------------------------------


Update a Omp Profile Parcel for System feature profile

.. code:: python

    def put(
        system_id: str,
        omp_id: str,
        payload: EditOmpProfileParcelForSystemPutRequest,
    ) -> EditOmpProfileParcelForSystemPutResponse: ...


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
        client.v1.feature_profile.sdwan.system.omp.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/omp/{ompId}
-------------------------------------------------------------------------------------


Delete a Omp Profile Parcel for System feature profile

.. code:: python

    def delete(system_id: str, omp_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.system.omp.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/omp
--------------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetListSdwanSystemOmpPayload: ...


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
        client.v1.feature_profile.sdwan.system.omp.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/omp/{ompId}
----------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, omp_id: str
    ) -> GetSingleSdwanSystemOmpPayload: ...


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
        client.v1.feature_profile.sdwan.system.omp.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

