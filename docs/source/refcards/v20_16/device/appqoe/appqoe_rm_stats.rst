=============================
device.appqoe.appqoe_rm_stats
=============================


Operation: GET /dataservice/device/appqoe/appqoe-rm-stats
---------------------------------------------------------


Get Appqoe RM Statistics from device

.. code:: python

    def get_appqoe_rm_stats(device_id: str) -> Any: ...


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
        client.device.appqoe.appqoe_rm_stats.get_appqoe_rm_stats()


