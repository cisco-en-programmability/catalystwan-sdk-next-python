======================================
device.vdsl_service.line_bonding_stats
======================================


Operation: GET /dataservice/device/vdslService/lineBondingStats
---------------------------------------------------------------


Get VDSL service line bonding stats from device

.. code:: python

    def get_line_bonding_stats(device_id: str) -> Any: ...


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
        client.device.vdsl_service.line_bonding_stats.get_line_bonding_stats()


