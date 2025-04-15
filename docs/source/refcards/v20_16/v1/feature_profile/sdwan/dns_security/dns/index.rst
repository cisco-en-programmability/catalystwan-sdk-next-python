=========================================
v1.feature_profile.sdwan.dns_security.dns
=========================================


Operation: POST /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns
--------------------------------------------------------------------------------------


Create Parcel for Sig Security Policy

.. code:: python

    def post(
        dns_security_id: str,
        payload: Union[
            CreateSigSecurityProfileParcelPostRequest1,
            CreateSigSecurityProfileParcelPostRequest2,
        ],
    ) -> CreateSigSecurityProfileParcelPostResponse: ...


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
        client.v1.feature_profile.sdwan.dns_security.dns.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns/{dnsSecurityProfileParcelId}
------------------------------------------------------------------------------------------------------------------


Update a Sig Security Profile Parcel

.. code:: python

    def put(
        dns_security_id: str,
        dns_security_profile_parcel_id: str,
        payload: Union[
            EditSigSecurityProfileParcelPutRequest1,
            EditSigSecurityProfileParcelPutRequest2,
        ],
    ) -> EditSigSecurityProfileParcelPutResponse: ...


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
        client.v1.feature_profile.sdwan.dns_security.dns.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns/{dnsSecurityProfileParcelId}
---------------------------------------------------------------------------------------------------------------------


Delete a SigSecurity Profile Parcel

.. code:: python

    def delete(
        dns_security_id: str, dns_security_profile_parcel_id: str
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
        client.v1.feature_profile.sdwan.dns_security.dns.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns
-------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        dns_security_id: str,
    ) -> GetListSdwanDnsSecurityDnsPayload: ...


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
        client.v1.feature_profile.sdwan.dns_security.dns.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns/{dnsSecurityProfileParcelId}
------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        dns_security_id: str, dns_security_profile_parcel_id: str
    ) -> GetSingleSdwanDnsSecurityDnsPayload: ...


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
        client.v1.feature_profile.sdwan.dns_security.dns.get()


.. toctree::
    :maxdepth: 1

    models

