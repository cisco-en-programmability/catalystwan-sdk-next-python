=========================================
v1.feature_profile.nfvirtual.networks.wan
=========================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/wan
-----------------------------------------------------------------------------------


Create a WAN Profile Parcel for Networks feature profile

.. code:: python

    def post(
        networks_id: str, payload: CreateNfvirtualWanParcelPostRequest
    ) -> CreateNfvirtualWanParcelPostResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.wan.post()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/wan/{wanId}
------------------------------------------------------------------------------------------


Get WAN Profile Parcels for Networks feature profile

.. code:: python

    def get(
        networks_id: str, wan_id: str
    ) -> GetSingleNfvirtualNetworksWanPayload: ...


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
        client.v1.feature_profile.nfvirtual.networks.wan.get()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/wan/{wanId}
------------------------------------------------------------------------------------------


Edit a WAN Profile Parcel for networks feature profile

.. code:: python

    def put(
        networks_id: str,
        wan_id: str,
        payload: EditNfvirtualWanParcelPutRequest,
    ) -> EditNfvirtualWanParcelPutResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.wan.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/wan/{wanId}
---------------------------------------------------------------------------------------------


Delete a WAN Profile Parcel for Networks feature profile

.. code:: python

    def delete(networks_id: str, wan_id: str) -> None: ...


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
        client.v1.feature_profile.nfvirtual.networks.wan.delete()


.. toctree::
    :maxdepth: 1

    models

