========================================
v1.feature_profile.sd_routing.system.aaa
========================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/aaa
--------------------------------------------------------------------------------


Create a SD-Routing AAA Feature for System Feature Profile

.. code:: python

    def post(
        system_id: str, payload: CreateSdroutingAaaFeaturePostRequest
    ) -> CreateSdroutingAaaFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.system.aaa.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/aaa/{aaaId}
---------------------------------------------------------------------------------------


Edit a SD-Routing AAA Feature for System Feature Profile

.. code:: python

    def put(
        system_id: str,
        aaa_id: str,
        payload: EditSdroutingAaaFeaturePutRequest,
    ) -> EditSdroutingAaaFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.system.aaa.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/aaa/{aaaId}
------------------------------------------------------------------------------------------


Delete a SD-Routing AAA Feature for System Feature Profile

.. code:: python

    def delete(system_id: str, aaa_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.system.aaa.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/aaa
-------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str,
    ) -> GetListSdRoutingSystemAaaSdRoutingPayload: ...


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
        client.v1.feature_profile.sd_routing.system.aaa.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/aaa/{aaaId}
---------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, aaa_id: str
    ) -> GetSingleSdRoutingSystemAaaSdRoutingPayload: ...


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
        client.v1.feature_profile.sd_routing.system.aaa.get()


.. toctree::
    :maxdepth: 1

    models

