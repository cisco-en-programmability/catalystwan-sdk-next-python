==========================================
v1.feature_profile.sdwan.embedded_security
==========================================


Operation: POST /dataservice/v1/feature-profile/sdwan/embedded-security
-----------------------------------------------------------------------


Create a SDWAN Embedded Security Feature Profile

.. code:: python

    def post(
        payload: Optional[
            CreateSdwanEmbeddedSecurityFeatureProfilePostRequest
        ] = None,
    ) -> CreateSdwanEmbeddedSecurityFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.sdwan.embedded_security.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/embedded-security/{embeddedSecurityId}
-------------------------------------------------------------------------------------------


Edit a SDWAN Embedded Security Feature Profile

.. code:: python

    def put(
        embedded_security_id: str,
        payload: Optional[
            EditSdwanEmbeddedSecurityFeatureProfilePutRequest
        ] = None,
    ) -> EditSdwanEmbeddedSecurityFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.sdwan.embedded_security.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/embedded-security/{embeddedSecurityId}
----------------------------------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete(embedded_security_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.embedded_security.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/embedded-security
----------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> List[GetSdwanEmbeddedSecurityFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.sdwan.embedded_security.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/embedded-security/{embeddedSecurityId}
-------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        embedded_security_id: str, details: Optional[bool] = False
    ) -> GetSingleSdwanEmbeddedSecurityPayload: ...


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
        client.v1.feature_profile.sdwan.embedded_security.get()


.. toctree::
    :maxdepth: 1

    policy/index
    unified/index
    models

