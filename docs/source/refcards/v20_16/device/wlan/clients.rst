===================
device.wlan.clients
===================


Operation: GET /dataservice/device/wlan/clients
-----------------------------------------------


Get WLAN client from device

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
        client.device.wlan.clients.get()


