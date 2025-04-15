=======================================
v1.feature_profile.sdwan.system.logging
=======================================


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/logging
-------------------------------------------------------------------------------


Create a Logging Profile Parcel for System feature profile

.. code:: python

    def post(
        system_id: str,
        payload: CreateLoggingProfileParcelForSystemPostRequest,
    ) -> CreateLoggingProfileParcelForSystemPostResponse: ...


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
        client.v1.feature_profile.sdwan.system.logging.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/logging/{loggingId}
------------------------------------------------------------------------------------------


Update a Logging Profile Parcel for System feature profile

.. code:: python

    def put(
        system_id: str,
        logging_id: str,
        payload: EditLoggingProfileParcelForSystemPutRequest,
    ) -> EditLoggingProfileParcelForSystemPutResponse: ...


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
        client.v1.feature_profile.sdwan.system.logging.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/logging/{loggingId}
---------------------------------------------------------------------------------------------


Delete a Logging Profile Parcel for System feature profile

.. code:: python

    def delete(system_id: str, logging_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.system.logging.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/logging
------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetListSdwanSystemLoggingPayload: ...


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
        client.v1.feature_profile.sdwan.system.logging.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/logging/{loggingId}
------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, logging_id: str
    ) -> GetSingleSdwanSystemLoggingPayload: ...


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
        client.v1.feature_profile.sdwan.system.logging.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

