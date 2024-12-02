============
device.stats
============


Operation: GET /dataservice/device/stats
----------------------------------------


Get stats queue information

.. code:: python

    def get_stats_queues() -> Any: ...


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
        client.device.stats.get_stats_queues()


