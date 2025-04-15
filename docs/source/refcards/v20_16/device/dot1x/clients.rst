====================
device.dot1x.clients
====================


Operation: GET /dataservice/device/dot1x/clients
------------------------------------------------


Get DOT1x client from device (Real Time)

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
        client.device.dot1x.clients.get()


