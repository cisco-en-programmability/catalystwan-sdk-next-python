=================================================
v1.feature_profile.sd_routing.service.dhcp_server
=================================================


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/dhcp-server
-----------------------------------------------------------------------------------------


Get all SD-Routing DHCP Server features in service feature profile

.. code:: python

    def get_sdrouting_dhcp_server_profile_parcels(
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
        client.v1.feature_profile.sd_routing.service.dhcp_server.get_sdrouting_dhcp_server_profile_parcels()


Operation: POST /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/dhcp-server
------------------------------------------------------------------------------------------


Create a SD-Routing DHCP Server feature in service feature profile

.. code:: python

    def create_sdrouting_dhcp_server_profile_parcel(
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
        client.v1.feature_profile.sd_routing.service.dhcp_server.create_sdrouting_dhcp_server_profile_parcel()


Operation: GET /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/dhcp-server/{dhcpServerId}
--------------------------------------------------------------------------------------------------------


Get a SD-Routing DHCP Server feature in service feature profile

.. code:: python

    def get_sdrouting_dhcp_server_profile_parcel(
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
        client.v1.feature_profile.sd_routing.service.dhcp_server.get_sdrouting_dhcp_server_profile_parcel()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/dhcp-server/{dhcpServerId}
--------------------------------------------------------------------------------------------------------


Edit a SD-Routing DHCP Server feature in service feature profile

.. code:: python

    def edit_sdrouting_dhcp_server_profile_parcel(
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
        client.v1.feature_profile.sd_routing.service.dhcp_server.edit_sdrouting_dhcp_server_profile_parcel()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/service/{serviceId}/dhcp-server/{dhcpServerId}
-----------------------------------------------------------------------------------------------------------


Delete a SD-Routing DHCP Server feature in service feature profile

.. code:: python

    def delete_sdrouting_dhcp_server_profile_parcel(
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
        client.v1.feature_profile.sd_routing.service.dhcp_server.delete_sdrouting_dhcp_server_profile_parcel()


