============================
device.action.test.ioxconfig
============================


Operation: GET /dataservice/device/action/test/ioxconfig/{deviceIP}
-------------------------------------------------------------------


testIoxConfig

.. code:: python

    def get(device_ip: DeviceIp) -> None: ...


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
        client.device.action.test.ioxconfig.get()


.. toctree::
    :maxdepth: 1

    models

