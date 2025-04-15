==============================================
v1.feature_profile.sd_routing.service.ipv4_acl
==============================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipv4-acl
---------------------------------------------------------------------------------------


Create a SD-Routing Ipv4 Acl Feature for Service Feature Profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateSdroutingServiceIpv4AclFeaturePostRequest,
    ) -> CreateSdroutingServiceIpv4AclFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.service.ipv4_acl.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipv4-acl/{ipv4AclId}
--------------------------------------------------------------------------------------------------


Edit a SD-Routing Ipv4 Acl Feature for Service Feature Profile

.. code:: python

    def put(
        service_id: str,
        ipv4_acl_id: str,
        payload: EditSdroutingServiceIpv4AclFeaturePutRequest,
    ) -> EditSdroutingServiceIpv4AclFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.service.ipv4_acl.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipv4-acl/{ipv4AclId}
-----------------------------------------------------------------------------------------------------


Delete a SD-Routing Ipv4 Acl Feature for Service Feature Profile

.. code:: python

    def delete(service_id: str, ipv4_acl_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.service.ipv4_acl.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipv4-acl
--------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(service_id: str) -> GetListSdRoutingServiceIpv4AclPayload: ...


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
        client.v1.feature_profile.sd_routing.service.ipv4_acl.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/ipv4-acl/{ipv4AclId}
--------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, ipv4_acl_id: str
    ) -> GetSingleSdRoutingServiceIpv4AclPayload: ...


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
        client.v1.feature_profile.sd_routing.service.ipv4_acl.get()


.. toctree::
    :maxdepth: 1

    models

