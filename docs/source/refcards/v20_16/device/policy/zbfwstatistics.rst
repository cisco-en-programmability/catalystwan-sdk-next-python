============================
device.policy.zbfwstatistics
============================


Operation: GET /dataservice/device/policy/zbfwstatistics
--------------------------------------------------------


Get zone based firewall statistics from device

.. code:: python

    def get_zbfw_statistics(device_id: str) -> Any: ...


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
        client.device.policy.zbfwstatistics.get_zbfw_statistics()


