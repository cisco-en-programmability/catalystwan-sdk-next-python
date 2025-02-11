===============================================
v1.feature_profile.sd_routing.embedded_security
===============================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/embedded-security
---------------------------------------------------------------------------


Get all SD-ROUTING Feature Profiles with giving Family and profile type

.. code:: python

    def get_sd_routing_embedded_security_feature_profiles(
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
        client.v1.feature_profile.sd_routing.embedded_security.get_sd_routing_embedded_security_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/sd-routing/embedded-security
----------------------------------------------------------------------------


Create a SD-ROUTING Embedded Security Feature Profile

.. code:: python

    def create_sd_routing_embedded_security_feature_profile(
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
        client.v1.feature_profile.sd_routing.embedded_security.create_sd_routing_embedded_security_feature_profile()


Operation: GET /dataservice/v1/feature-profile/sd-routing/embedded-security/{embeddedSecurityId}
------------------------------------------------------------------------------------------------


Get a SD-ROUTING Embedded Security Feature Profile with embeddedSecurityId

.. code:: python

    def get_sd_routing_embedded_security_feature_profile_by_profile_id(
        embedded_security_id: str,
        details: Optional[bool] = False,
        references: Optional[bool] = False,
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
        client.v1.feature_profile.sd_routing.embedded_security.get_sd_routing_embedded_security_feature_profile_by_profile_id()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/embedded-security/{embeddedSecurityId}
------------------------------------------------------------------------------------------------


Edit a SD-ROUTING Embedded Security Feature Profile

.. code:: python

    def edit_sd_routing_embedded_security_feature_profile(
        embedded_security_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.embedded_security.edit_sd_routing_embedded_security_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/embedded-security/{embeddedSecurityId}
---------------------------------------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete_sd_routing_embedded_security_feature_profile(
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
        client.v1.feature_profile.sd_routing.embedded_security.delete_sd_routing_embedded_security_feature_profile()


.. toctree::
    :maxdepth: 1

    policy
    unified/index

