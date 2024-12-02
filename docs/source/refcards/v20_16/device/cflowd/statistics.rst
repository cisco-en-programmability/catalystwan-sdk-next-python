========================
device.cflowd.statistics
========================


Operation: GET /dataservice/device/cflowd/statistics
----------------------------------------------------


Get cflowd statistics from device

.. code:: python

    def create_cflowd_statistics(device_id: str) -> Any: ...


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
        client.device.cflowd.statistics.create_cflowd_statistics()


