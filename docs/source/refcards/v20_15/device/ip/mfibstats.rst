===================
device.ip.mfibstats
===================


Operation: GET /dataservice/device/ip/mfibstats
-----------------------------------------------


Get IP MFIB statistics list from device (Real Time)

.. code:: python

    def create_ip_mfib_stats_list(device_id: str) -> Any: ...


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
        client.device.ip.mfibstats.create_ip_mfib_stats_list()


