===================================
v1.feature_profile.sdwan.system.aaa
===================================


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/aaa
---------------------------------------------------------------------------


Create a Aaa Profile Parcel for System feature profile

.. code:: python

    def post(
        system_id: str,
        payload: CreateAaaProfileParcelForSystemPostRequest,
    ) -> CreateAaaProfileParcelForSystemPostResponse: ...


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
        client.v1.feature_profile.sdwan.system.aaa.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/aaa/{aaaId}
----------------------------------------------------------------------------------


Update a Aaa Profile Parcel for System feature profile

.. code:: python

    def put(
        system_id: str,
        aaa_id: str,
        payload: EditAaaProfileParcelForSystemPutRequest,
    ) -> EditAaaProfileParcelForSystemPutResponse: ...


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
        client.v1.feature_profile.sdwan.system.aaa.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/aaa/{aaaId}
-------------------------------------------------------------------------------------


Delete a Aaa Profile Parcel for System feature profile

.. code:: python

    def delete(system_id: str, aaa_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.system.aaa.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/aaa
--------------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetListSdwanSystemAaaPayload: ...


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
        client.v1.feature_profile.sdwan.system.aaa.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/aaa/{aaaId}
----------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, aaa_id: str
    ) -> GetSingleSdwanSystemAaaPayload: ...


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
        client.v1.feature_profile.sdwan.system.aaa.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

