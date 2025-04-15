===============================================
v1.feature_profile.sd_routing.embedded_security
===============================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/embedded-security
----------------------------------------------------------------------------


Create a SD-ROUTING Embedded Security Feature Profile

.. code:: python

    def post(
        payload: CreateSdRoutingEmbeddedSecurityFeatureProfilePostRequest,
    ) -> CreateSdRoutingEmbeddedSecurityFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.sd_routing.embedded_security.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/embedded-security/{embeddedSecurityId}
------------------------------------------------------------------------------------------------


Edit a SD-ROUTING Embedded Security Feature Profile

.. code:: python

    def put(
        embedded_security_id: str,
        payload: EditSdRoutingEmbeddedSecurityFeatureProfilePutRequest,
    ) -> EditSdRoutingEmbeddedSecurityFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.sd_routing.embedded_security.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/embedded-security/{embeddedSecurityId}
---------------------------------------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete(embedded_security_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.embedded_security.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/embedded-security
---------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None,
        limit: Optional[int] = 0,
        reference_count: Optional[bool] = False,
    ) -> List[GetSdRoutingEmbeddedSecurityFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.sd_routing.embedded_security.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/embedded-security/{embeddedSecurityId}
------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        embedded_security_id: str,
        details: Optional[bool] = False,
        references: Optional[bool] = False,
    ) -> GetSingleSdRoutingEmbeddedSecurityPayload: ...


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
        client.v1.feature_profile.sd_routing.embedded_security.get()


.. toctree::
    :maxdepth: 1

    policy/index
    unified/index
    models

