==========================
device.tcpopt.expiredflows
==========================


Operation: GET /dataservice/device/tcpopt/expiredflows
------------------------------------------------------


Get TCP optimized expired flows from device (Real Time)

.. code:: python

    def get_expired_tcp_flows(device_id: str) -> Any: ...


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
        client.device.tcpopt.expiredflows.get_expired_tcp_flows()


