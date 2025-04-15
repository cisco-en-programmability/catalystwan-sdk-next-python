================================================
v1.feature_profile.nfvirtual.networks.ovsnetwork
================================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/ovsnetwork
------------------------------------------------------------------------------------------


Create OVS Network Profile Parcel for Networks feature profile

.. code:: python

    def post(
        networks_id: str,
        payload: CreateNfvirtualOvsNetworkParcelPostRequest,
    ) -> CreateNfvirtualOvsNetworkParcelPostResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.ovsnetwork.post()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/ovsnetwork/{ovsNetworkId}
--------------------------------------------------------------------------------------------------------


Edit a OVS Network Profile Parcel for Networks feature profile

.. code:: python

    def put(
        networks_id: str,
        ovs_network_id: str,
        payload: EditNfvirtualOvsNetworkParcelPutRequest,
    ) -> EditNfvirtualOvsNetworkParcelPutResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.ovsnetwork.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/ovsnetwork/{ovsNetworkId}
-----------------------------------------------------------------------------------------------------------


Delete a OVS Network Profile Parcel for Networks feature profile

.. code:: python

    def delete(networks_id: str, ovs_network_id: str) -> None: ...


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
        client.v1.feature_profile.nfvirtual.networks.ovsnetwork.delete()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/ovsnetwork/{networkId}
----------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        network_id: str, details: bool
    ) -> GetSingleNfvirtualNetworksOvsnetworkPayload: ...


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
        client.v1.feature_profile.nfvirtual.networks.ovsnetwork.get()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/ovsnetwork/{ovsNetworkId}
--------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        networks_id: str, ovs_network_id: str
    ) -> GetSingleNfvirtualNetworksOvsnetworkPayload: ...


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
        client.v1.feature_profile.nfvirtual.networks.ovsnetwork.get()


.. toctree::
    :maxdepth: 1

    models

