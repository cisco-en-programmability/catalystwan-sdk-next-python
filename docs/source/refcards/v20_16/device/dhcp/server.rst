==================
device.dhcp.server
==================


Operation: GET /dataservice/device/dhcp/server
----------------------------------------------


Get DHCP server from device (Real Time)

.. code:: python

    def get_dhcp_server(device_id: str) -> Any: ...


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
        client.device.dhcp.server.get_dhcp_server()


