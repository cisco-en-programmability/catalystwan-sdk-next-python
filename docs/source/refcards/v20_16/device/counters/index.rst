===============
device.counters
===============


Operation: GET /dataservice/device/counters
-------------------------------------------


Get device counters

.. code:: python

    def get_device_counters() -> DeviceCountersResponse: ...


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
        client.device.counters.get_device_counters()


.. toctree::
    :maxdepth: 1

    models

