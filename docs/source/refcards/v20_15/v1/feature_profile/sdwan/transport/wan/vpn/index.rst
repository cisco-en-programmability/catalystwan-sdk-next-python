==========================================
v1.feature_profile.sdwan.transport.wan.vpn
==========================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn
------------------------------------------------------------------------------------


Get Wan Vpn Profile Parcels for Transport feature profile

.. code:: python

    def get_wan_vpn_profile_parcel_for_transport(
        transport_id: str,
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.get_wan_vpn_profile_parcel_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn
-------------------------------------------------------------------------------------


Create a Wan Vpn Profile Parcel for Transport feature profile

.. code:: python

    def create_wan_vpn_profile_parcel_for_transport(
        transport_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.create_wan_vpn_profile_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}
--------------------------------------------------------------------------------------------


Get Wan Vpn Profile Parcel by parcelId for Transport feature profile

.. code:: python

    def get_wan_vpn_profile_parcel_by_parcel_id_for_transport(
        transport_id: str, vpn_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.get_wan_vpn_profile_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}
--------------------------------------------------------------------------------------------


Update a Wan Vpn Profile Parcel for Transport feature profile

.. code:: python

    def edit_wan_vpn_profile_parcel_for_transport(
        transport_id: str, vpn_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.edit_wan_vpn_profile_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/wan/vpn/{vpnId}
-----------------------------------------------------------------------------------------------


Delete a Wan Vpn Profile Parcel for Transport feature profile

.. code:: python

    def delete_wan_vpn_profile_parcel_for_transport(
        transport_id: str, vpn_id: str
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
        client.v1.feature_profile.sdwan.transport.wan.vpn.delete_wan_vpn_profile_parcel_for_transport()


.. toctree::
    :maxdepth: 1

    interface/index
    schema/index
    routing/index

