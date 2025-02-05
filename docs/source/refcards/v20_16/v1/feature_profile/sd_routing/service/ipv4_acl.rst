==============================================
v1.feature_profile.sd_routing.service.ipv4_acl
==============================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipv4-acl
--------------------------------------------------------------------------------------


Get all SD-Routing IPv4 ACL features from a specific service feature profile

.. code:: python

    def get_sdrouting_service_ipv4_acl_features(
        service_id: str,
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
        client.v1.feature_profile.sd_routing.service.ipv4_acl.get_sdrouting_service_ipv4_acl_features()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipv4-acl
---------------------------------------------------------------------------------------


Create a SD-Routing IPv4 ACL feature from a specific service feature profile

.. code:: python

    def create_sdrouting_service_ipv4_acl_feature(
        service_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.service.ipv4_acl.create_sdrouting_service_ipv4_acl_feature()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipv4-acl/{ipv4AclId}
--------------------------------------------------------------------------------------------------


Get the SD-Routing IPv4 ACL feature from a specific service feature profile

.. code:: python

    def get_sdrouting_service_ipv4_acl_feature(
        service_id: str, ipv4_acl_id: str
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
        client.v1.feature_profile.sd_routing.service.ipv4_acl.get_sdrouting_service_ipv4_acl_feature()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipv4-acl/{ipv4AclId}
--------------------------------------------------------------------------------------------------


Edit the SD-Routing IPv4 ACL feature from a specific service feature profile

.. code:: python

    def edit_sdrouting_service_ipv4_acl_feature(
        service_id: str, ipv4_acl_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.service.ipv4_acl.edit_sdrouting_service_ipv4_acl_feature()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipv4-acl/{ipv4AclId}
-----------------------------------------------------------------------------------------------------


Delete the SD-Routing IPv4 ACL feature from a specific service feature profile

.. code:: python

    def delete_sdrouting_service_ipv4_acl_feature(
        service_id: str, ipv4_acl_id: str
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
        client.v1.feature_profile.sd_routing.service.ipv4_acl.delete_sdrouting_service_ipv4_acl_feature()


