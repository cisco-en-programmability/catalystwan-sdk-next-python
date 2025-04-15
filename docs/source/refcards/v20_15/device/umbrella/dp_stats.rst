========================
device.umbrella.dp_stats
========================


Operation: GET /dataservice/device/umbrella/dp-stats
----------------------------------------------------


Get Umbrella dp-stats from device

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
        client.device.umbrella.dp_stats.get()


