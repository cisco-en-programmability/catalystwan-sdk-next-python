=========================================
v1.feature_profile.nfvirtual.networks.lan
=========================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/lan
-----------------------------------------------------------------------------------


Create LAN Profile Parcel for Networks feature profile

.. code:: python

    def create_nfvirtual_lan_parcel(
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
        client.v1.feature_profile.nfvirtual.networks.lan.create_nfvirtual_lan_parcel()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/lan/{lanId}
------------------------------------------------------------------------------------------


Get LAN Profile Parcels for Networks feature profile

.. code:: python

    def get_nfvirtual_lan_parcel(
        networks_id: str, lan_id: str
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
        client.v1.feature_profile.nfvirtual.networks.lan.get_nfvirtual_lan_parcel()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/lan/{lanId}
------------------------------------------------------------------------------------------


Edit a  LAN Profile Parcel for networks feature profile

.. code:: python

    def edit_nfvirtual_lan_parcel(
        networks_id: str, lan_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.nfvirtual.networks.lan.edit_nfvirtual_lan_parcel()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/lan/{lanId}
---------------------------------------------------------------------------------------------


Delete a LAN Profile Parcel for Networks feature profile

.. code:: python

    def delete_nfvirtual_lan_parcel(
        networks_id: str, lan_id: str
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
        client.v1.feature_profile.nfvirtual.networks.lan.delete_nfvirtual_lan_parcel()


