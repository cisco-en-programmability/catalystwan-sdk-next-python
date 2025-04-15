=============================
device.hardware.synced.alarms
=============================


Operation: GET /dataservice/device/hardware/synced/alarms
---------------------------------------------------------


Get hardware alarm list synchronously from device

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
        client.device.hardware.synced.alarms.get()


