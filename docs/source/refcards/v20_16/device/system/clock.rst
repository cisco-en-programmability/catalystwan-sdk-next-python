===================
device.system.clock
===================


Operation: GET /dataservice/device/system/clock
-----------------------------------------------


Get device system clock

.. code:: python

    def get_device_system_clock(device_id: str) -> Any: ...


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
        client.device.system.clock.get_device_system_clock()


