===================================
v1.feature_profile.nfvirtual.system
===================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/system
----------------------------------------------------------------


Create a nfvirtual System Feature Profile

.. code:: python

    def post(
        payload: CreateNfvirtualSystemFeatureProfilePostRequest,
    ) -> CreateNfvirtualSystemFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.nfvirtual.system.post()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/system/{systemId}
--------------------------------------------------------------------------


Edit a Nfvirtual System Feature Profile

.. code:: python

    def put(
        system_id: str,
        payload: EditNfvirtualSystemFeatureProfilePutRequest,
    ) -> EditNfvirtualSystemFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.nfvirtual.system.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/system/{systemId}
-----------------------------------------------------------------------------


Delete a Nfvirtual System Feature Profile

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
        client.v1.feature_profile.nfvirtual.system.delete()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system
---------------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> List[GetAllNfvirtualSystemFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.nfvirtual.system.get()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system/{systemId}
--------------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetSingleNfvirtualSystemPayload: ...


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
        client.v1.feature_profile.nfvirtual.system.get()


.. toctree::
    :maxdepth: 1

    aaa/index
    banner/index
    logging/index
    ntp/index
    snmp/index
    system_settings/index
    models

