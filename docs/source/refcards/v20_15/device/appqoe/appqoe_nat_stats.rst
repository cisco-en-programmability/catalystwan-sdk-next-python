==============================
device.appqoe.appqoe_nat_stats
==============================


Operation: GET /dataservice/device/appqoe/appqoe-nat-stats
----------------------------------------------------------


Get Appqoe Nat Statistics from device

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
        client.device.appqoe.appqoe_nat_stats.get()


