=============================
colocation.monitor.device.vnf
=============================


Operation: GET /dataservice/colocation/monitor/device/vnf
---------------------------------------------------------


Deprecated!!!

List all VNF attached with Device

.. code:: python

    def get(device_id: DeviceUuid) -> None: ...


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
        client.colocation.monitor.device.vnf.get()


.. toctree::
    :maxdepth: 1

    models

