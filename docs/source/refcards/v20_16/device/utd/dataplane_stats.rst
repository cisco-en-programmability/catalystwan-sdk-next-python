==========================
device.utd.dataplane_stats
==========================


Operation: GET /dataservice/device/utd/dataplane-stats
------------------------------------------------------


Get data plane stats from Device

.. code:: python

    def get_utd_dataplane_stats(device_id: str) -> Any: ...


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
        client.device.utd.dataplane_stats.get_utd_dataplane_stats()


