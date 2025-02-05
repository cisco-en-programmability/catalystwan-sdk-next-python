=======================
device.crashlog.details
=======================


Operation: GET /dataservice/device/crashlog/details
---------------------------------------------------


Get device crash logs for all device

.. code:: python

    def get_all_device_crash_logs() -> Any: ...


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
        client.device.crashlog.details.get_all_device_crash_logs()


