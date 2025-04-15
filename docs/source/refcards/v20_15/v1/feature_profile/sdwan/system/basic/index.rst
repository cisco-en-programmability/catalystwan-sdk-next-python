=====================================
v1.feature_profile.sdwan.system.basic
=====================================


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/basic
-----------------------------------------------------------------------------


Create a Basic Profile Feature for System feature profile

.. code:: python

    def post(
        system_id: str,
        payload: CreateBasicProfileFeatureForSystemPostRequest,
    ) -> CreateBasicProfileFeatureForSystemPostResponse: ...


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
        client.v1.feature_profile.sdwan.system.basic.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/basic/{basicId}
--------------------------------------------------------------------------------------


Update a Basic Profile Feature for System feature profile

.. code:: python

    def put(
        system_id: str,
        basic_id: str,
        payload: EditBasicProfileFeatureForSystemPutRequest,
    ) -> EditBasicProfileFeatureForSystemPutResponse: ...


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
        client.v1.feature_profile.sdwan.system.basic.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/basic/{basicId}
-----------------------------------------------------------------------------------------


Delete a Basic Profile Feature for System feature profile

.. code:: python

    def delete(system_id: str, basic_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.system.basic.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/basic
----------------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetListSdwanSystemBasicPayload: ...


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
        client.v1.feature_profile.sdwan.system.basic.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/basic/{basicId}
--------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, basic_id: str
    ) -> GetSingleSdwanSystemBasicPayload: ...


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
        client.v1.feature_profile.sdwan.system.basic.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

