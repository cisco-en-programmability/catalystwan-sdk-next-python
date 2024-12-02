======================
device.crashlog.synced
======================


Operation: GET /dataservice/device/crashlog/synced
--------------------------------------------------


Get device crash logs synchronously from device

.. code:: python

    def get_device_crash_logs_synced(device_id: str) -> Any: ...


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
        client.device.crashlog.synced.get_device_crash_logs_synced()


