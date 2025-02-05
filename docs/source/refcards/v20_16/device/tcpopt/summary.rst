=====================
device.tcpopt.summary
=====================


Operation: GET /dataservice/device/tcpopt/summary
-------------------------------------------------


Get TCP optimization summary from device (Real Time)

.. code:: python

    def get_tcp_summary(device_id: str) -> Any: ...


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
        client.device.tcpopt.summary.get_tcp_summary()


