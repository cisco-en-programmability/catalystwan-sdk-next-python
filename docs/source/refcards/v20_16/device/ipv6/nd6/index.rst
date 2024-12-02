===============
device.ipv6.nd6
===============


Operation: GET /dataservice/device/ipv6/nd6
-------------------------------------------


Get ipv6 data from device

.. code:: python

    def get_ipv6_data(device_id: DeviceIp) -> Any: ...


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
        client.device.ipv6.nd6.get_ipv6_data()


.. toctree::
    :maxdepth: 1

    models

