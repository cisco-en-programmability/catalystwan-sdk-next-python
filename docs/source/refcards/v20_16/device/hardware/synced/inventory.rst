================================
device.hardware.synced.inventory
================================


Operation: GET /dataservice/device/hardware/synced/inventory
------------------------------------------------------------


Get hardware inventory list synchronously from device

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
        client.device.hardware.synced.inventory.get()


