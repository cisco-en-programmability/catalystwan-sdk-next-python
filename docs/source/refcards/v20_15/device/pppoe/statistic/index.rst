======================
device.pppoe.statistic
======================


Operation: GET /dataservice/device/pppoe/statistic
--------------------------------------------------


Get PPPoE statistics from device

.. code:: python

    def get(device_id: DeviceIp) -> Any: ...


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
        client.device.pppoe.statistic.get()


.. toctree::
    :maxdepth: 1

    models

