=========================================
v1.feature_profile.sdwan.dns_security.dns
=========================================


Operation: GET /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns
-------------------------------------------------------------------------------------


Get Sig Security Profile Parcels for a given ParcelType

.. code:: python

    def get_sig_security_profile_parcel(dns_security_id: str) -> str: ...


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
        client.v1.feature_profile.sdwan.dns_security.dns.get_sig_security_profile_parcel()


Operation: POST /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns
--------------------------------------------------------------------------------------


Create Parcel for Sig Security Policy

.. code:: python

    def create_sig_security_profile_parcel(
        dns_security_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.dns_security.dns.create_sig_security_profile_parcel()


Operation: GET /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns/{dnsSecurityProfileParcelId}
------------------------------------------------------------------------------------------------------------------


Get SigSecurity Profile Parcel by parcelId

.. code:: python

    def get_sig_security_profile_parcel_by_parcel_id(
        dns_security_id: str, dns_security_profile_parcel_id: str
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.dns_security.dns.get_sig_security_profile_parcel_by_parcel_id()


Operation: PUT /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns/{dnsSecurityProfileParcelId}
------------------------------------------------------------------------------------------------------------------


Update a Sig Security Profile Parcel

.. code:: python

    def edit_sig_security_profile_parcel(
        dns_security_id: str,
        dns_security_profile_parcel_id: str,
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.dns_security.dns.edit_sig_security_profile_parcel()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}/dns/{dnsSecurityProfileParcelId}
---------------------------------------------------------------------------------------------------------------------


Delete a SigSecurity Profile Parcel

.. code:: python

    def delete_sig_security_profile_parcel(
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
        client.v1.feature_profile.sdwan.dns_security.dns.delete_sig_security_profile_parcel()


