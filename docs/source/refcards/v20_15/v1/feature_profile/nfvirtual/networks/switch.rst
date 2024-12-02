============================================
v1.feature_profile.nfvirtual.networks.switch
============================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/switch
--------------------------------------------------------------------------------------


Create Switch Profile config for Networks feature profile

.. code:: python

    def create_nfvirtual_switch_parcel(
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
        client.v1.feature_profile.nfvirtual.networks.switch.create_nfvirtual_switch_parcel()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/switch/{switchId}
------------------------------------------------------------------------------------------------


Get Switch Profile Parcels for Networks feature profile

.. code:: python

    def get_nfvirtual_switch_parcel(
        networks_id: str, switch_id: str
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
        client.v1.feature_profile.nfvirtual.networks.switch.get_nfvirtual_switch_parcel()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/switch/{switchId}
------------------------------------------------------------------------------------------------


Edit a Switch Profile Parcel for networks feature profile

.. code:: python

    def edit_nfvirtual_switch_parcel(
        networks_id: str, switch_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.nfvirtual.networks.switch.edit_nfvirtual_switch_parcel()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/switch/{switchId}
---------------------------------------------------------------------------------------------------


Delete Switch Profile config for Networks feature profile

.. code:: python

    def delete_nfvirtual_switch_parcel(
        networks_id: str, switch_id: str
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
        client.v1.feature_profile.nfvirtual.networks.switch.delete_nfvirtual_switch_parcel()


