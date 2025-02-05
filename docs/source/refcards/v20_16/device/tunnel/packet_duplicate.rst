==============================
device.tunnel.packet_duplicate
==============================


Operation: GET /dataservice/device/tunnel/packet-duplicate
----------------------------------------------------------


Get tunnel statistics packet duplication statistics

.. code:: python

    def create_packet_duplicate_statistics(device_id: str) -> Any: ...


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
        client.device.tunnel.packet_duplicate.create_packet_duplicate_statistics()


