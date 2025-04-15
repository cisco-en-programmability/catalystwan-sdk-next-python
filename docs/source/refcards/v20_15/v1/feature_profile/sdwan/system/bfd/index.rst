===================================
v1.feature_profile.sdwan.system.bfd
===================================


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/bfd
---------------------------------------------------------------------------


Create a Bfd Profile Parcel for System feature profile

.. code:: python

    def post(
        system_id: str,
        payload: CreateBfdProfileParcelForSystemPostRequest,
    ) -> CreateBfdProfileParcelForSystemPostResponse: ...


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
        client.v1.feature_profile.sdwan.system.bfd.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/bfd/{bfdId}
----------------------------------------------------------------------------------


Update a Bfd Profile Parcel for System feature profile

.. code:: python

    def put(
        system_id: str,
        bfd_id: str,
        payload: EditBfdProfileParcelForSystemPutRequest,
    ) -> EditBfdProfileParcelForSystemPutResponse: ...


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
        client.v1.feature_profile.sdwan.system.bfd.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/bfd/{bfdId}
-------------------------------------------------------------------------------------


Delete a Bfd Profile Parcel for System feature profile

.. code:: python

    def delete(system_id: str, bfd_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.system.bfd.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/bfd
--------------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetListSdwanSystemBfdPayload: ...


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
        client.v1.feature_profile.sdwan.system.bfd.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/bfd/{bfdId}
----------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, bfd_id: str
    ) -> GetSingleSdwanSystemBfdPayload: ...


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
        client.v1.feature_profile.sdwan.system.bfd.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

