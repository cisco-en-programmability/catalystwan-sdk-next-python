=============================
device.vdsl_service.cpe_stats
=============================


Operation: GET /dataservice/device/vdslService/cpeStats
-------------------------------------------------------


Get CPE stats from device

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
        client.device.vdsl_service.cpe_stats.get()


