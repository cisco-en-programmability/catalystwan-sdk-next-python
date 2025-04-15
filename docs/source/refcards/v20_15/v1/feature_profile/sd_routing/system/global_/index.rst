============================================
v1.feature_profile.sd_routing.system.global_
============================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/global
-----------------------------------------------------------------------------------


Create a SD-Routing Global Setting Feature for System Feature Profile

.. code:: python

    def post(
        system_id: str,
        payload: CreateSdroutingGlobalSettingFeaturePostRequest,
    ) -> CreateSdroutingGlobalSettingFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.system.global_.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/global/{globalId}
---------------------------------------------------------------------------------------------


Edit a SD-Routing Global Setting Feature for System Feature Profile

.. code:: python

    def put(
        system_id: str,
        global_id: str,
        payload: EditSdroutingGlobalSettingFeaturePutRequest,
    ) -> EditSdroutingGlobalSettingFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.system.global_.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/global/{globalId}
------------------------------------------------------------------------------------------------


Delete a SD-Routing Global Setting Feature for System Feature Profile

.. code:: python

    def delete(system_id: str, global_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.system.global_.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/global
----------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetListSdRoutingSystemGlobalPayload: ...


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
        client.v1.feature_profile.sd_routing.system.global_.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/global/{globalId}
---------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, global_id: str
    ) -> GetSingleSdRoutingSystemGlobalPayload: ...


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
        client.v1.feature_profile.sd_routing.system.global_.get()


.. toctree::
    :maxdepth: 1

    models

