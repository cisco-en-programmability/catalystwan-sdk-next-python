================================
device.policy.zbfwdropstatistics
================================


Operation: GET /dataservice/device/policy/zbfwdropstatistics
------------------------------------------------------------


Get zone drop statistics from device

.. code:: python

    def get_zone_drop_statistics(device_id: str) -> Any: ...


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
        client.device.policy.zbfwdropstatistics.get_zone_drop_statistics()


