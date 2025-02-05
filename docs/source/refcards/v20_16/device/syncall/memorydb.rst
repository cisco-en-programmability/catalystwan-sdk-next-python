=======================
device.syncall.memorydb
=======================


Operation: POST /dataservice/device/syncall/memorydb
----------------------------------------------------


Synchronize memory database for all devices

.. code:: python

    def sync_all_devices_mem_db() -> None: ...


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
        client.device.syncall.memorydb.sync_all_devices_mem_db()


