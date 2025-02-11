============================================
v1.feature_profile.nfvirtual.networks.routes
============================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/routes
--------------------------------------------------------------------------------------


Create Routes Profile config for Networks feature profile

.. code:: python

    def create_nfvirtual_routes_parcel(
        networks_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.nfvirtual.networks.routes.create_nfvirtual_routes_parcel()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/routes/{routesId}
------------------------------------------------------------------------------------------------


Get Routes Profile Parcels for Networks feature profile

.. code:: python

    def get_nfvirtual_routes_parcel(
        networks_id: str, routes_id: str
    ) -> str: ...


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
        client.v1.feature_profile.nfvirtual.networks.routes.get_nfvirtual_routes_parcel()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/routes/{routesId}
------------------------------------------------------------------------------------------------


Edit a Routes Profile Parcel for networks feature profile

.. code:: python

    def edit_nfvirtual_routes_parcel(
        networks_id: str, routes_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.nfvirtual.networks.routes.edit_nfvirtual_routes_parcel()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/routes/{routesId}
---------------------------------------------------------------------------------------------------


Delete Routes Profile config for Networks feature profile

.. code:: python

    def delete_nfvirtual_routes_parcel(
        networks_id: str, routes_id: str
    ) -> None: ...


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
        client.v1.feature_profile.nfvirtual.networks.routes.delete_nfvirtual_routes_parcel()


