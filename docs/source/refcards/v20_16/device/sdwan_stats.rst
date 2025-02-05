==================
device.sdwan_stats
==================


Operation: GET /dataservice/device/sdwan-stats
----------------------------------------------


Get SD-WAN statistics detail from device (Real Time)

.. code:: python

    def get_sd_wan_stats(device_id: str) -> Any: ...


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
        client.device.sdwan_stats.get_sd_wan_stats()


