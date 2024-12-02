=============================================================
v1.feature_profile.sd_routing.transport.multicloud_connection
=============================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection
-------------------------------------------------------------------------------------------------------


Get Lan Vpn Profile Parcels for Service feature profile

.. code:: python

    def get_lan_vpn_profile_parcel_for_service_1(
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
        client.v1.feature_profile.sd_routing.transport.multicloud_connection.get_lan_vpn_profile_parcel_for_service_1()


Operation: POST /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection
--------------------------------------------------------------------------------------------------------


Associate a MultiCloudConnection Parcel for transport feature profile

.. code:: python

    def create_multi_cloud_connection_1(
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
        client.v1.feature_profile.sd_routing.transport.multicloud_connection.create_multi_cloud_connection_1()


Operation: GET /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection/{multiCloudConnectionId}
--------------------------------------------------------------------------------------------------------------------------------


Get Lan Vpn Profile Parcel by parcelId for Service feature profile

.. code:: python

    def get_lan_vpn_profile_parcel_by_parcel_id_for_service_1(
        transport_id: str, multi_cloud_connection_id: str
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
        client.v1.feature_profile.sd_routing.transport.multicloud_connection.get_lan_vpn_profile_parcel_by_parcel_id_for_service_1()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection/{multiCloudConnectionId}
--------------------------------------------------------------------------------------------------------------------------------


Update a multicloud connection parcel

.. code:: python

    def edit_multi_cloud_connection_1(
        transport_id: str,
        multi_cloud_connection_id: str,
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
        client.v1.feature_profile.sd_routing.transport.multicloud_connection.edit_multi_cloud_connection_1()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/transport/{transportId}/multicloud-connection/{multiCloudConnectionId}
-----------------------------------------------------------------------------------------------------------------------------------


Delete a MultiCloud Connection Profile Parcel for Transport feature profile

.. code:: python

    def delete_multi_cloud_connection_parcel_for_transport(
        transport_id: str, multi_cloud_connection_id: str
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
        client.v1.feature_profile.sd_routing.transport.multicloud_connection.delete_multi_cloud_connection_parcel_for_transport()


.. toctree::
    :maxdepth: 1

    schema/index

