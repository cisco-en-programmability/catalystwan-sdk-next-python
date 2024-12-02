========================
device.tunnel.statistics
========================


Operation: GET /dataservice/device/tunnel/statistics
----------------------------------------------------


Get tunnel statistics all devices

.. code:: python

    def create_statistics_list(device_id: str) -> Any: ...


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
        client.device.tunnel.statistics.create_statistics_list()


