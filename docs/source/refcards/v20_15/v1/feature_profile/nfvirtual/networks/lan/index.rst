=========================================
v1.feature_profile.nfvirtual.networks.lan
=========================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/lan
-----------------------------------------------------------------------------------


Create LAN Profile Parcel for Networks feature profile

.. code:: python

    def post(
        networks_id: str, payload: CreateNfvirtualLanParcelPostRequest
    ) -> CreateNfvirtualLanParcelPostResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.lan.post()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/lan/{lanId}
------------------------------------------------------------------------------------------


Get LAN Profile Parcels for Networks feature profile

.. code:: python

    def get(
        networks_id: str, lan_id: str
    ) -> GetSingleNfvirtualNetworksLanPayload: ...


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
        client.v1.feature_profile.nfvirtual.networks.lan.get()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/lan/{lanId}
------------------------------------------------------------------------------------------


Edit a  LAN Profile Parcel for networks feature profile

.. code:: python

    def put(
        networks_id: str,
        lan_id: str,
        payload: EditNfvirtualLanParcelPutRequest,
    ) -> EditNfvirtualLanParcelPutResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.lan.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/lan/{lanId}
---------------------------------------------------------------------------------------------


Delete a LAN Profile Parcel for Networks feature profile

.. code:: python

    def delete(networks_id: str, lan_id: str) -> None: ...


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
        client.v1.feature_profile.nfvirtual.networks.lan.delete()


.. toctree::
    :maxdepth: 1

    models

