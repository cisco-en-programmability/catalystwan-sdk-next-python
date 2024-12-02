=========================
device.tcpopt.activeflows
=========================


Operation: GET /dataservice/device/tcpopt/activeflows
-----------------------------------------------------


Get TCP optimized active flows from device (Real Time)

.. code:: python

    def get_active_tcp_flows(device_id: str) -> Any: ...


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
        client.device.tcpopt.activeflows.get_active_tcp_flows()


