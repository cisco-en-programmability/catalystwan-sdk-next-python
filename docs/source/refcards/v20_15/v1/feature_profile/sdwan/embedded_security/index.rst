==========================================
v1.feature_profile.sdwan.embedded_security
==========================================


Operation: GET /dataservice/v1/feature-profile/sdwan/embedded-security
----------------------------------------------------------------------


Get all SDWAN Feature Profiles with giving Family and profile type

.. code:: python

    def get_sdwan_embedded_security_feature_profiles(
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
        client.v1.feature_profile.sdwan.embedded_security.get_sdwan_embedded_security_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/sdwan/embedded-security
-----------------------------------------------------------------------


Create a SDWAN Embedded Security Feature Profile

.. code:: python

    def create_sdwan_embedded_security_feature_profile(
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
        client.v1.feature_profile.sdwan.embedded_security.create_sdwan_embedded_security_feature_profile()


Operation: GET /dataservice/v1/feature-profile/sdwan/embedded-security/{embeddedSecurityId}
-------------------------------------------------------------------------------------------


Get a SDWAN Embedded Security Feature Profile with embeddedSecurityId

.. code:: python

    def get_sdwan_embedded_security_feature_profile_by_profile_id(
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
        client.v1.feature_profile.sdwan.embedded_security.get_sdwan_embedded_security_feature_profile_by_profile_id()


Operation: PUT /dataservice/v1/feature-profile/sdwan/embedded-security/{embeddedSecurityId}
-------------------------------------------------------------------------------------------


Edit a SDWAN Embedded Security Feature Profile

.. code:: python

    def edit_sdwan_embedded_security_feature_profile(
        embedded_security_id: str,
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
        client.v1.feature_profile.sdwan.embedded_security.edit_sdwan_embedded_security_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/embedded-security/{embeddedSecurityId}
----------------------------------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete_sdwan_embedded_security_feature_profile(
        embedded_security_id: str,
    ) -> None: ...


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
        client.v1.feature_profile.sdwan.embedded_security.delete_sdwan_embedded_security_feature_profile()


.. toctree::
    :maxdepth: 1

    policy/index
    unified/index
    models

