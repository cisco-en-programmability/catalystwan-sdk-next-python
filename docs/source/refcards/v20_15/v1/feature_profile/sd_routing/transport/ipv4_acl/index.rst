================================================
v1.feature_profile.sd_routing.transport.ipv4_acl
================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/ipv4-acl
-------------------------------------------------------------------------------------------


Create a SD-Routing Ipv4 Acl Feature for Transport Feature Profile

.. code:: python

    def post(
        transport_id: str,
        payload: CreateSdroutingTransportIpv4AclFeaturePostRequest,
    ) -> CreateSdroutingTransportIpv4AclFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.ipv4_acl.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/ipv4-acl/{ipv4AclId}
------------------------------------------------------------------------------------------------------


Edit a SD-Routing Ipv4 Acl Feature for Transport Feature Profile

.. code:: python

    def put(
        transport_id: str,
        ipv4_acl_id: str,
        payload: EditSdroutingTransportIpv4AclFeaturePutRequest,
    ) -> EditSdroutingTransportIpv4AclFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.transport.ipv4_acl.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/ipv4-acl/{ipv4AclId}
---------------------------------------------------------------------------------------------------------


Delete a SD-Routing Ipv4 Acl Feature for Transport Feature Profile

.. code:: python

    def delete(transport_id: str, ipv4_acl_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.transport.ipv4_acl.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/ipv4-acl
------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str,
    ) -> GetListSdRoutingTransportIpv4AclPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.ipv4_acl.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/ipv4-acl/{ipv4AclId}
------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        transport_id: str, ipv4_acl_id: str
    ) -> GetSingleSdRoutingTransportIpv4AclPayload: ...


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
        client.v1.feature_profile.sd_routing.transport.ipv4_acl.get()


.. toctree::
    :maxdepth: 1

    models

