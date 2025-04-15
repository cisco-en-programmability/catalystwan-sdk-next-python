=================================================
v1.feature_profile.sdwan.embedded_security.policy
=================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/policy
-------------------------------------------------------------------------------------------


Create Feature for Security Policy

.. code:: python

    def post(
        security_id: str,
        payload: CreateSdwanEmbeddedSecurityFeaturePostRequest,
    ) -> CreateSdwanEmbeddedSecurityFeaturePostResponse: ...


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
        client.v1.feature_profile.sdwan.embedded_security.policy.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/policy/{securityProfileParcelId}
--------------------------------------------------------------------------------------------------------------------


Update a Security Feature

.. code:: python

    def put(
        security_id: str,
        security_profile_parcel_id: str,
        payload: EditSdwanSecurityFeaturePutRequest,
    ) -> EditSdwanSecurityFeaturePutResponse: ...


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
        client.v1.feature_profile.sdwan.embedded_security.policy.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/policy/{securityProfileParcelId}
-----------------------------------------------------------------------------------------------------------------------


Delete a Security Feature

.. code:: python

    def delete(
        security_id: str, security_profile_parcel_id: str
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
        client.v1.feature_profile.sdwan.embedded_security.policy.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/policy
------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        security_id: str,
    ) -> GetListSdwanEmbeddedSecurityPolicyPayload: ...


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
        client.v1.feature_profile.sdwan.embedded_security.policy.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/policy/{securityProfileParcelId}
--------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        security_id: str, security_profile_parcel_id: str
    ) -> GetSingleSdwanEmbeddedSecurityPolicyPayload: ...


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
        client.v1.feature_profile.sdwan.embedded_security.policy.get()


.. toctree::
    :maxdepth: 1

    models

