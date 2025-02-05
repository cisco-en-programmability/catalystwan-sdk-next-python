=====================================
v1.feature_profile.sdwan.dns_security
=====================================


Operation: GET /dataservice/v1/feature-profile/sdwan/dns-security
-----------------------------------------------------------------


Get all SDWAN Feature Profiles with giving Family and profile type

.. code:: python

    def get_sdwan_dns_security_feature_profiles(
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        reference_count: Optional[bool] = False,
    ) -> Any: ...


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
        client.v1.feature_profile.sdwan.dns_security.get_sdwan_dns_security_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/sdwan/dns-security
------------------------------------------------------------------


Create a SDWAN Dns Security Feature Profile

.. code:: python

    def create_sdwan_dns_security_feature_profile(
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
        client.v1.feature_profile.sdwan.dns_security.create_sdwan_dns_security_feature_profile()


Operation: GET /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}
---------------------------------------------------------------------------------


Get a SDWAN Dns Security Feature Profile with dnsSecurityId

.. code:: python

    def get_sdwan_dns_security_feature_profile_by_profile_id(
        dns_security_id: str, references: Optional[bool] = False
    ) -> Any: ...


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
        client.v1.feature_profile.sdwan.dns_security.get_sdwan_dns_security_feature_profile_by_profile_id()


Operation: PUT /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}
---------------------------------------------------------------------------------


Edit a SDWAN Dns Security Feature Profile

.. code:: python

    def edit_sdwan_dns_security_feature_profile(
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
        client.v1.feature_profile.sdwan.dns_security.edit_sdwan_dns_security_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/dns-security/{dnsSecurityId}
------------------------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete_sdwan_dns_security_feature_profile(
        dns_security_id: str,
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
        client.v1.feature_profile.sdwan.dns_security.delete_sdwan_dns_security_feature_profile()


.. toctree::
    :maxdepth: 1

    dns

