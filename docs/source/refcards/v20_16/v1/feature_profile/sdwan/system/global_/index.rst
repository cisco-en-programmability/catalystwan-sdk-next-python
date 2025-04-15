=======================================
v1.feature_profile.sdwan.system.global_
=======================================


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/global
------------------------------------------------------------------------------


Create a Global Profile Parcel for System feature profile

.. code:: python

    def post(
        system_id: str,
        payload: CreateGlobalProfileParcelForSystemPostRequest,
    ) -> CreateGlobalProfileParcelForSystemPostResponse: ...


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
        client.v1.feature_profile.sdwan.system.global_.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/global/{globalId}
----------------------------------------------------------------------------------------


Update a Global Profile Parcel for System feature profile

.. code:: python

    def put(
        system_id: str,
        global_id: str,
        payload: EditGlobalProfileParcelForSystemPutRequest,
    ) -> EditGlobalProfileParcelForSystemPutResponse: ...


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
        client.v1.feature_profile.sdwan.system.global_.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/global/{globalId}
-------------------------------------------------------------------------------------------


Delete a Global Profile Parcel for System feature profile

.. code:: python

    def delete(system_id: str, global_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.system.global_.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/global
-----------------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetListSdwanSystemGlobalPayload: ...


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
        client.v1.feature_profile.sdwan.system.global_.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/global/{globalId}
----------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, global_id: str
    ) -> GetSingleSdwanSystemGlobalPayload: ...


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
        client.v1.feature_profile.sdwan.system.global_.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

