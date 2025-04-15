==================================
device.utd.dataplane_stats_summary
==================================


Operation: GET /dataservice/device/utd/dataplane-stats-summary
--------------------------------------------------------------


Get data plane stats summary

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
        client.device.utd.dataplane_stats_summary.get()


