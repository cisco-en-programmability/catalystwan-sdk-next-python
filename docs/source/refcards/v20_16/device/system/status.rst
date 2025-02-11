====================
device.system.status
====================


Operation: GET /dataservice/device/system/status
------------------------------------------------


Get device system status list (Real Time)

.. code:: python

    def create_device_system_status_list(device_id: str) -> Any: ...


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
        client.device.system.status.create_device_system_status_list()


