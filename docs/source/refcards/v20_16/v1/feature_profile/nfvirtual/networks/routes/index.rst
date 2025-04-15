============================================
v1.feature_profile.nfvirtual.networks.routes
============================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/routes
--------------------------------------------------------------------------------------


Create Routes Profile config for Networks feature profile

.. code:: python

    def post(
        networks_id: str, payload: CreateNfvirtualRoutesParcelPostRequest
    ) -> CreateNfvirtualRoutesParcelPostResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.routes.post()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/routes/{routesId}
------------------------------------------------------------------------------------------------


Get Routes Profile Parcels for Networks feature profile

.. code:: python

    def get(
        networks_id: str, routes_id: str
    ) -> GetSingleNfvirtualNetworksRoutesPayload: ...


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
        client.v1.feature_profile.nfvirtual.networks.routes.get()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/routes/{routesId}
------------------------------------------------------------------------------------------------


Edit a Routes Profile Parcel for networks feature profile

.. code:: python

    def put(
        networks_id: str,
        routes_id: str,
        payload: EditNfvirtualRoutesParcelPutRequest,
    ) -> EditNfvirtualRoutesParcelPutResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.routes.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/routes/{routesId}
---------------------------------------------------------------------------------------------------


Delete Routes Profile config for Networks feature profile

.. code:: python

    def delete(networks_id: str, routes_id: str) -> None: ...


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
        client.v1.feature_profile.nfvirtual.networks.routes.delete()


.. toctree::
    :maxdepth: 1

    models

