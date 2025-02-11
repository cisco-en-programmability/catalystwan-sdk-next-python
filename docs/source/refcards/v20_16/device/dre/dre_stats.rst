====================
device.dre.dre_stats
====================


Operation: GET /dataservice/device/dre/dre-stats
------------------------------------------------


Get DRE statistics

.. code:: python

    def get_dre_stats(device_id: str) -> Any: ...


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
        client.device.dre.dre_stats.get_dre_stats()


