================================================
v1.feature_profile.nfvirtual.networks.ovsnetwork
================================================


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/ovsnetwork/{networkId}
----------------------------------------------------------------------------------------


Get all Nfvirtual OVS Networks Feature Profile with networkId

.. code:: python

    def get_all_nfvirtual_ovs_networks_feature_profile_by_profile_id(
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
        client.v1.feature_profile.nfvirtual.networks.ovsnetwork.get_all_nfvirtual_ovs_networks_feature_profile_by_profile_id()


Operation: POST /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/ovsnetwork
------------------------------------------------------------------------------------------


Create OVS Network Profile Parcel for Networks feature profile

.. code:: python

    def create_nfvirtual_ovs_network_parcel(
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
        client.v1.feature_profile.nfvirtual.networks.ovsnetwork.create_nfvirtual_ovs_network_parcel()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/ovsnetwork/{ovsNetworkId}
--------------------------------------------------------------------------------------------------------


Get OVS Network Profile Parcels for Networks feature profile

.. code:: python

    def get_nfvirtual_ovs_network_parcel(
        networks_id: str, ovs_network_id: str
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
        client.v1.feature_profile.nfvirtual.networks.ovsnetwork.get_nfvirtual_ovs_network_parcel()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/ovsnetwork/{ovsNetworkId}
--------------------------------------------------------------------------------------------------------


Edit a OVS Network Profile Parcel for Networks feature profile

.. code:: python

    def edit_nfvirtual_ovs_network_parcel(
        networks_id: str,
        ovs_network_id: str,
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
        client.v1.feature_profile.nfvirtual.networks.ovsnetwork.edit_nfvirtual_ovs_network_parcel()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/ovsnetwork/{ovsNetworkId}
-----------------------------------------------------------------------------------------------------------


Delete a OVS Network Profile Parcel for Networks feature profile

.. code:: python

    def delete_nfvirtual_ovs_network_parcel(
        networks_id: str, ovs_network_id: str
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
        client.v1.feature_profile.nfvirtual.networks.ovsnetwork.delete_nfvirtual_ovs_network_parcel()


