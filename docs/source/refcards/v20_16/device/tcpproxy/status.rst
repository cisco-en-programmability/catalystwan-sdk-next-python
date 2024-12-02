======================
device.tcpproxy.status
======================


Operation: GET /dataservice/device/tcpproxy/status
--------------------------------------------------


Get tcp proxy status from device

.. code:: python

    def get_tcp_proxy_status(device_id: str) -> Any: ...


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
        client.device.tcpproxy.status.get_tcp_proxy_status()


