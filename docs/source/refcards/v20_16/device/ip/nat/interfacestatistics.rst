=================================
device.ip.nat.interfacestatistics
=================================


Operation: GET /dataservice/device/ip/nat/interfacestatistics
-------------------------------------------------------------


Get NAT interface statistics list from device

.. code:: python

    def get(device_id: str) -> Any: ...


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
        client.device.ip.nat.interfacestatistics.get()


