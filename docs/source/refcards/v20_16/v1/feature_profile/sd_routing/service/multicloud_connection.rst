===========================================================
v1.feature_profile.sd_routing.service.multicloud_connection
===========================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/multicloud-connection
---------------------------------------------------------------------------------------------------


Get Multicloud Connection Profile Parcels for Service feature profile

.. code:: python

    def get_list_of_profile_parcels(service_id: str) -> str: ...


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
        client.v1.feature_profile.sd_routing.service.multicloud_connection.get_list_of_profile_parcels()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/multicloud-connection
----------------------------------------------------------------------------------------------------


Associate a MultiCloudConnection Parcel for service feature profile

.. code:: python

    def create_multi_cloud_connection(
        service_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.sd_routing.service.multicloud_connection.create_multi_cloud_connection()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/multicloud-connection/{multiCloudConnectionId}
----------------------------------------------------------------------------------------------------------------------------


Get a multicloud connection parcel

.. code:: python

    def get_multi_cloud_connection(
        service_id: str, multi_cloud_connection_id: str
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
        client.v1.feature_profile.sd_routing.service.multicloud_connection.get_multi_cloud_connection()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/multicloud-connection/{multiCloudConnectionId}
----------------------------------------------------------------------------------------------------------------------------


Update a multicloud connection parcel

.. code:: python

    def edit_multi_cloud_connection(
        service_id: str,
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
        client.v1.feature_profile.sd_routing.service.multicloud_connection.edit_multi_cloud_connection()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/multicloud-connection/{multiCloudConnectionId}
-------------------------------------------------------------------------------------------------------------------------------


Delete a MultiCloud Connection Profile Parcel for Service feature profile

.. code:: python

    def delete_multi_cloud_connection_parcel_for_service(
        service_id: str, multi_cloud_connection_id: str
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
        client.v1.feature_profile.sd_routing.service.multicloud_connection.delete_multi_cloud_connection_parcel_for_service()


