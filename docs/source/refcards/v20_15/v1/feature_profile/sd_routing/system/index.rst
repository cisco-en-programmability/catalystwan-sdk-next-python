====================================
v1.feature_profile.sd_routing.system
====================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/system
-----------------------------------------------------------------


Create a SD-Routing System Feature Profile

.. code:: python

    def post(
        payload: CreateSdroutingSystemFeatureProfilePostRequest,
    ) -> CreateSdroutingSystemFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.sd_routing.system.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}
---------------------------------------------------------------------------


Edit a SD-Routing System Feature Profile

.. code:: python

    def put(
        system_id: str,
        payload: EditSdroutingSystemFeatureProfilePutRequest,
    ) -> EditSdroutingSystemFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.sd_routing.system.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}
------------------------------------------------------------------------------


Delete a SD-Routing System Feature Profile

.. code:: python

    def delete(system_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.system.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system
----------------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> List[GetSdroutingSystemFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.sd_routing.system.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}
---------------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetSingleSdRoutingSystemPayload: ...


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
        client.v1.feature_profile.sd_routing.system.get()


.. toctree::
    :maxdepth: 1

    aaa/index
    banner/index
    certificate/index
    flexible_port_speed/index
    global_/index
    logging/index
    ntp/index
    snmp/index
    models

