===================
device.crashlog.log
===================


Operation: GET /dataservice/device/crashlog/log
-----------------------------------------------


Get device crash info from device

.. code:: python

    def get_device_crash_information(
        device_id: str, filename: str
    ) -> str: ...


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
        client.device.crashlog.log.get_device_crash_information()


