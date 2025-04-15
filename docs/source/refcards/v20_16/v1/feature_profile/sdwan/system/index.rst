===============================
v1.feature_profile.sdwan.system
===============================


Operation: POST /dataservice/v1/feature-profile/sdwan/system
------------------------------------------------------------


Create a SDWAN System Feature Profile

.. code:: python

    def post(
        payload: CreateSdwanSystemFeatureProfilePostRequest,
    ) -> CreateSdwanSystemFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.sdwan.system.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}
----------------------------------------------------------------------


Edit a SDWAN System Feature Profile

.. code:: python

    def put(
        system_id: str, payload: EditSdwanSystemFeatureProfilePutRequest
    ) -> EditSdwanSystemFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.sdwan.system.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}
-------------------------------------------------------------------------


Delete Feature Profile

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
        client.v1.feature_profile.sdwan.system.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/system
-----------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> List[GetSdwanSystemFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.sdwan.system.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}
----------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetSingleSdwanSystemPayload: ...


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
        client.v1.feature_profile.sdwan.system.get()


.. toctree::
    :maxdepth: 1

    aaa/index
    banner/index
    basic/index
    bfd/index
    global_/index
    logging/index
    mrf/index
    ntp/index
    omp/index
    snmp/index
    security/index
    models

