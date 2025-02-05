=================================================
v1.feature_profile.sdwan.transport.management.vpn
=================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn
-------------------------------------------------------------------------------------------


Get Management Vpn Profile Parcels for Transport feature profile

.. code:: python

    def get_management_vpn_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.management.vpn.get_management_vpn_profile_parcel_for_transport()


Operation: POST /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn
--------------------------------------------------------------------------------------------


Create a Management Vpn Profile Parcel for Transport feature profile

.. code:: python

    def create_management_vpn_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.management.vpn.create_management_vpn_profile_parcel_for_transport()


Operation: GET /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}
---------------------------------------------------------------------------------------------------


Get Management Vpn Profile Parcel by parcelId for Transport feature profile

.. code:: python

    def get_management_vpn_profile_parcel_by_parcel_id_for_transport(
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
        client.v1.feature_profile.sdwan.transport.management.vpn.get_management_vpn_profile_parcel_by_parcel_id_for_transport()


Operation: PUT /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}
---------------------------------------------------------------------------------------------------


Update a Management Vpn Profile Parcel for Transport feature profile

.. code:: python

    def edit_management_vpn_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.management.vpn.edit_management_vpn_profile_parcel_for_transport()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/transport/{transportId}/management/vpn/{vpnId}
------------------------------------------------------------------------------------------------------


Delete a Management Vpn Profile Parcel for Transport feature profile

.. code:: python

    def delete_management_vpn_profile_parcel_for_transport(
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
        client.v1.feature_profile.sdwan.transport.management.vpn.delete_management_vpn_profile_parcel_for_transport()


.. toctree::
    :maxdepth: 1

    interface/index
    schema/index

