============================================
v1.feature_profile.nfvirtual.networks.switch
============================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/switch
--------------------------------------------------------------------------------------


Create Switch Profile config for Networks feature profile

.. code:: python

    def post(
        networks_id: str, payload: CreateNfvirtualSwitchParcelPostRequest
    ) -> CreateNfvirtualSwitchParcelPostResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.switch.post()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/switch/{switchId}
------------------------------------------------------------------------------------------------


Get Switch Profile Parcels for Networks feature profile

.. code:: python

    def get(
        networks_id: str, switch_id: str
    ) -> GetSingleNfvirtualNetworksSwitchPayload: ...


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
        client.v1.feature_profile.nfvirtual.networks.switch.get()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/switch/{switchId}
------------------------------------------------------------------------------------------------


Edit a Switch Profile Parcel for networks feature profile

.. code:: python

    def put(
        networks_id: str,
        switch_id: str,
        payload: EditNfvirtualSwitchParcelPutRequest,
    ) -> EditNfvirtualSwitchParcelPutResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.switch.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/switch/{switchId}
---------------------------------------------------------------------------------------------------


Delete Switch Profile config for Networks feature profile

.. code:: python

    def delete(networks_id: str, switch_id: str) -> None: ...


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
        client.v1.feature_profile.nfvirtual.networks.switch.delete()


.. toctree::
    :maxdepth: 1

    models

