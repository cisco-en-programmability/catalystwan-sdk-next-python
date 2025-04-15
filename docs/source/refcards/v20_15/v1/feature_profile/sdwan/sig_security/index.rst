=====================================
v1.feature_profile.sdwan.sig_security
=====================================


Operation: POST /dataservice/v1/feature-profile/sdwan/sig-security
------------------------------------------------------------------


Create a SDWAN Sig Security Feature Profile

.. code:: python

    def post(
        payload: CreateSdwanSigSecurityFeatureProfilePostRequest,
    ) -> CreateSdwanSigSecurityFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.sdwan.sig_security.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}
---------------------------------------------------------------------------------


Edit a SDWAN Sig Security Feature Profile

.. code:: python

    def put(
        sig_security_id: str,
        payload: EditSdwanSigSecurityFeatureProfilePutRequest,
    ) -> EditSdwanSigSecurityFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.sdwan.sig_security.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}
------------------------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete(sig_security_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.sig_security.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/sig-security
-----------------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        reference_count: Optional[bool] = False,
    ) -> List[GetSdwanSigSecurityFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.sdwan.sig_security.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/sig-security/{sigSecurityId}
---------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        sig_security_id: str, references: Optional[bool] = False
    ) -> GetSingleSdwanSigSecurityPayload: ...


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
        client.v1.feature_profile.sdwan.sig_security.get()


.. toctree::
    :maxdepth: 1

    sig/index
    models

