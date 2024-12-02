=========================================
v1.feature_profile.nfvirtual.networks.wan
=========================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/wan
-----------------------------------------------------------------------------------


Create a WAN Profile Parcel for Networks feature profile

.. code:: python

    def create_nfvirtual_wan_parcel(
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
        client.v1.feature_profile.nfvirtual.networks.wan.create_nfvirtual_wan_parcel()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/wan/{wanId}
------------------------------------------------------------------------------------------


Get WAN Profile Parcels for Networks feature profile

.. code:: python

    def get_nfvirtual_wan_parcel(
        networks_id: str, wan_id: str
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
        client.v1.feature_profile.nfvirtual.networks.wan.get_nfvirtual_wan_parcel()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/wan/{wanId}
------------------------------------------------------------------------------------------


Edit a WAN Profile Parcel for networks feature profile

.. code:: python

    def edit_nfvirtual_wan_parcel(
        networks_id: str, wan_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.nfvirtual.networks.wan.edit_nfvirtual_wan_parcel()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/wan/{wanId}
---------------------------------------------------------------------------------------------


Delete a WAN Profile Parcel for Networks feature profile

.. code:: python

    def delete_nfvirtual_wan_parcel(
        networks_id: str, wan_id: str
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
        client.v1.feature_profile.nfvirtual.networks.wan.delete_nfvirtual_wan_parcel()


