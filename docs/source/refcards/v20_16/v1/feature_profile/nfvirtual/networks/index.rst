=====================================
v1.feature_profile.nfvirtual.networks
=====================================


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks
-----------------------------------------------------------------


Get all Nfvirtual Feature Profiles

.. code:: python

    def get_all_nfvirtual_networks_feature_profiles(
        offset: int, limit: int
    ) -> Any: ...


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
        client.v1.feature_profile.nfvirtual.networks.get_all_nfvirtual_networks_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/nfvirtual/networks
------------------------------------------------------------------


Create a nfvirtual Networks Feature Profile

.. code:: python

    def create_nfvirtual_networks_feature_profile(
        payload: Optional[str] = None,
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
        client.v1.feature_profile.nfvirtual.networks.create_nfvirtual_networks_feature_profile()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/{networkId}
-----------------------------------------------------------------------------


Get a Nfvirtual Networks Feature Profile with networkId

.. code:: python

    def get_nfvirtual_networks_feature_profile_by_profile_id(
        network_id: str, details: bool
    ) -> Any: ...


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
        client.v1.feature_profile.nfvirtual.networks.get_nfvirtual_networks_feature_profile_by_profile_id()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/networks/{networkId}
-----------------------------------------------------------------------------


Edit a Nfvirtual Networks Feature Profile

.. code:: python

    def edit_nfvirtual_networks_feature_profile(
        network_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.nfvirtual.networks.edit_nfvirtual_networks_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/networks/{networkId}
--------------------------------------------------------------------------------


Delete a Nfvirtual Networks Feature Profile

.. code:: python

    def delete_nfvirtual_networks_feature_profile(
        network_id: str,
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
        client.v1.feature_profile.nfvirtual.networks.delete_nfvirtual_networks_feature_profile()


.. toctree::
    :maxdepth: 1

    ovsnetwork
    lan
    routes
    switch
    vnf_attributes/index
    wan

