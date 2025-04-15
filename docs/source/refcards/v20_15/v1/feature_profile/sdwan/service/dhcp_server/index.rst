============================================
v1.feature_profile.sdwan.service.dhcp_server
============================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/dhcp-server
-------------------------------------------------------------------------------------


Create a Dhcp Server Profile Parcel for Service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateDhcpServerProfileParcelForServicePostRequest,
    ) -> CreateDhcpServerProfileParcelForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.dhcp_server.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/dhcp-server/{dhcpServerId}
---------------------------------------------------------------------------------------------------


Update a Dhcp Server Profile Parcel for Service feature profile

.. code:: python

    def put(
        service_id: str,
        dhcp_server_id: str,
        payload: EditDhcpServerProfileParcelForServicePutRequest,
    ) -> EditDhcpServerProfileParcelForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.dhcp_server.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/dhcp-server/{dhcpServerId}
------------------------------------------------------------------------------------------------------


Delete a Dhcp Server Profile Parcel for Service feature profile

.. code:: python

    def delete(service_id: str, dhcp_server_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.dhcp_server.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/dhcp-server
------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(service_id: str) -> GetListSdwanServiceDhcpServerPayload: ...


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
        client.v1.feature_profile.sdwan.service.dhcp_server.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/dhcp-server/{dhcpServerId}
---------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, dhcp_server_id: str
    ) -> GetSingleSdwanServiceDhcpServerPayload: ...


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
        client.v1.feature_profile.sdwan.service.dhcp_server.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

