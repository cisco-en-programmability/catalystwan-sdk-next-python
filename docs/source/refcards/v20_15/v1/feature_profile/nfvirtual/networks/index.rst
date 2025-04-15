=====================================
v1.feature_profile.nfvirtual.networks
=====================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/networks
------------------------------------------------------------------


Create a nfvirtual Networks Feature Profile

.. code:: python

    def post(
        payload: CreateNfvirtualNetworksFeatureProfilePostRequest,
    ) -> CreateNfvirtualNetworksFeatureProfilePostResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.post()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/networks/{networkId}
-----------------------------------------------------------------------------


Edit a Nfvirtual Networks Feature Profile

.. code:: python

    def put(
        network_id: str,
        payload: EditNfvirtualNetworksFeatureProfilePutRequest,
    ) -> EditNfvirtualNetworksFeatureProfilePutResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/networks/{networkId}
--------------------------------------------------------------------------------


Delete a Nfvirtual Networks Feature Profile

.. code:: python

    def delete(network_id: str) -> None: ...


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
        client.v1.feature_profile.nfvirtual.networks.delete()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks
-----------------------------------------------------------------


.. code:: python

    @overload
    def get(
        offset: int, limit: int
    ) -> List[GetAllNfvirtualNetworksFeatureProfilesGetResponse]: ...


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
        client.v1.feature_profile.nfvirtual.networks.get()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/{networkId}
-----------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        network_id: str, details: bool
    ) -> GetSingleNfvirtualNetworksPayload: ...


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
        client.v1.feature_profile.nfvirtual.networks.get()


.. toctree::
    :maxdepth: 1

    ovsnetwork/index
    lan/index
    routes/index
    switch/index
    vnf_attributes/index
    wan/index
    models

