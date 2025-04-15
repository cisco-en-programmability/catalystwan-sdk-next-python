=============================================================
v1.feature_profile.sdwan.embedded_security.unified.ngfirewall
=============================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/unified/ngfirewall
-------------------------------------------------------------------------------------------------------


Create Feature for Ngfirewall Policy

.. code:: python

    def post(
        security_id: str, payload: CreateSdwanNgfirewallFeaturePostRequest
    ) -> CreateSdwanNgfirewallFeaturePostResponse: ...


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
        client.v1.feature_profile.sdwan.embedded_security.unified.ngfirewall.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/unified/ngfirewall/{securityProfileParcelId}
--------------------------------------------------------------------------------------------------------------------------------


Update a Ngfirewall Feature

.. code:: python

    def put(
        security_id: str,
        security_profile_parcel_id: str,
        payload: EditSdwanNgfirewallFeaturePutRequest,
    ) -> EditSdwanNgfirewallFeaturePutResponse: ...


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
        client.v1.feature_profile.sdwan.embedded_security.unified.ngfirewall.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/unified/ngfirewall/{securityProfileParcelId}
-----------------------------------------------------------------------------------------------------------------------------------


Delete a Ngfirewall Feature

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
        client.v1.feature_profile.sdwan.embedded_security.unified.ngfirewall.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/unified/ngfirewall
------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        security_id: str,
    ) -> GetListSdwanEmbeddedSecurityUnifiedNgfirewallPayload: ...


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
        client.v1.feature_profile.sdwan.embedded_security.unified.ngfirewall.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/embedded-security/{securityId}/unified/ngfirewall/{securityProfileParcelId}
--------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        security_id: str, security_profile_parcel_id: str
    ) -> GetSingleSdwanEmbeddedSecurityUnifiedNgfirewallPayload: ...


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
        client.v1.feature_profile.sdwan.embedded_security.unified.ngfirewall.get()


.. toctree::
    :maxdepth: 1

    models

