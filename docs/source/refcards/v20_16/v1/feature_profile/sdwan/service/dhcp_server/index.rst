============================================
v1.feature_profile.sdwan.service.dhcp_server
============================================


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/dhcp-server
------------------------------------------------------------------------------------


Get Dhcp Server Profile Parcels for Service feature profile

.. code:: python

    def get_dhcp_server_profile_parcel_for_service(
        service_id: str,
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
        client.v1.feature_profile.sdwan.service.dhcp_server.get_dhcp_server_profile_parcel_for_service()


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/dhcp-server
-------------------------------------------------------------------------------------


Create a Dhcp Server Profile Parcel for Service feature profile

.. code:: python

    def create_dhcp_server_profile_parcel_for_service(
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
        client.v1.feature_profile.sdwan.service.dhcp_server.create_dhcp_server_profile_parcel_for_service()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/dhcp-server/{dhcpServerId}
---------------------------------------------------------------------------------------------------


Get Dhcp Server Profile Parcel by parcelId for Service feature profile

.. code:: python

    def get_dhcp_server_profile_parcel_by_parcel_id_for_service(
        service_id: str, dhcp_server_id: str
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
        client.v1.feature_profile.sdwan.service.dhcp_server.get_dhcp_server_profile_parcel_by_parcel_id_for_service()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/dhcp-server/{dhcpServerId}
---------------------------------------------------------------------------------------------------


Update a Dhcp Server Profile Parcel for Service feature profile

.. code:: python

    def edit_dhcp_server_profile_parcel_for_service(
        service_id: str,
        dhcp_server_id: str,
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
        client.v1.feature_profile.sdwan.service.dhcp_server.edit_dhcp_server_profile_parcel_for_service()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/dhcp-server/{dhcpServerId}
------------------------------------------------------------------------------------------------------


Delete a Dhcp Server Profile Parcel for Service feature profile

.. code:: python

    def delete_dhcp_server_profile_parcel_for_service(
        service_id: str, dhcp_server_id: str
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
        client.v1.feature_profile.sdwan.service.dhcp_server.delete_dhcp_server_profile_parcel_for_service()


.. toctree::
    :maxdepth: 1

    schema/index

