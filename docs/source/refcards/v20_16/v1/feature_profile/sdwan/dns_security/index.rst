=====================================
v1.feature_profile.sdwan.dns_security
=====================================


Operation: POST /dataservice/v1/feature-profile/sdwan/dns-security
------------------------------------------------------------------


Create a SDWAN Dns Security Feature Profile

.. code:: python

    def post(
        payload: CreateSdwanDnsSecurityFeatureProfilePostRequest,
    ) -> CreateSdwanDnsSecurityFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.sdwan.dns_security.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}
---------------------------------------------------------------------------------


Edit a SDWAN Dns Security Feature Profile

.. code:: python

    def put(
        dns_security_id: str,
        payload: EditSdwanDnsSecurityFeatureProfilePutRequest,
    ) -> EditSdwanDnsSecurityFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.sdwan.dns_security.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}
------------------------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete(dns_security_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.dns_security.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/dns-security
-----------------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        reference_count: Optional[bool] = False,
    ) -> List[GetSdwanDnsSecurityFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.sdwan.dns_security.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}
---------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        dns_security_id: str, references: Optional[bool] = False
    ) -> GetSingleSdwanDnsSecurityPayload: ...


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
        client.v1.feature_profile.sdwan.dns_security.get()


.. toctree::
    :maxdepth: 1

    dns/index
    models

