==========================
dca.device.crashlog.synced
==========================


Operation: GET /dataservice/dca/device/crashlog/synced
------------------------------------------------------


Get device crash log

.. code:: python

    def get_crash_logs_synced(device_id: str) -> Any: ...


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
        client.dca.device.crashlog.synced.get_crash_logs_synced()


