========================================
v1.feature_profile.sdwan.system.security
========================================


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/security
--------------------------------------------------------------------------------


Create Security for System feature profile

.. code:: python

    def post(
        system_id: str, payload: CreateSecurityForSystemPostRequest
    ) -> CreateSecurityForSystemPostResponse: ...


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
        client.v1.feature_profile.sdwan.system.security.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/security/{securityId}
--------------------------------------------------------------------------------------------


Update Security for System feature profile

.. code:: python

    def put(
        system_id: str,
        security_id: str,
        payload: EditSecurityForSystemPutRequest,
    ) -> EditSecurityForSystemPutResponse: ...


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
        client.v1.feature_profile.sdwan.system.security.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/security/{securityId}
-----------------------------------------------------------------------------------------------


Delete Security for System feature profile

.. code:: python

    def delete(system_id: str, security_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.system.security.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/security
-------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetListSdwanSystemSecurityPayload: ...


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
        client.v1.feature_profile.sdwan.system.security.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/security/{securityId}
--------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, security_id: str
    ) -> GetSingleSdwanSystemSecurityPayload: ...


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
        client.v1.feature_profile.sdwan.system.security.get()


.. toctree::
    :maxdepth: 1

    models

