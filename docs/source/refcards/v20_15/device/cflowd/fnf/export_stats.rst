==============================
device.cflowd.fnf.export_stats
==============================


Operation: GET /dataservice/device/cflowd/fnf/export-stats
----------------------------------------------------------


Get FnF export stats from device

.. code:: python

    def get(device_id: str) -> Any: ...


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
        client.device.cflowd.fnf.export_stats.get()


