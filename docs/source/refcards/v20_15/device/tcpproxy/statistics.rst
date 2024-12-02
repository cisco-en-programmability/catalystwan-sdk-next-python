==========================
device.tcpproxy.statistics
==========================


Operation: GET /dataservice/device/tcpproxy/statistics
------------------------------------------------------


Get tcp proxy statistics from device

.. code:: python

    def get_tcp_proxy_statistics(device_id: str) -> Any: ...


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
        client.device.tcpproxy.statistics.get_tcp_proxy_statistics()


