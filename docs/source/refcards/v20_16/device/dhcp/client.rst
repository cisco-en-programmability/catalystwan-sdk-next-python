==================
device.dhcp.client
==================


Operation: GET /dataservice/device/dhcp/client
----------------------------------------------


Get DHCP client from device (Real Time)

.. code:: python

    def get_dhcp_client(device_id: str) -> Any: ...


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
        client.device.dhcp.client.get_dhcp_client()


