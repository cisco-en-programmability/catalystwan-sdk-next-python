==========================
device.sig.zscaler.tunnels
==========================


Operation: GET /dataservice/device/sig/zscaler/tunnels
------------------------------------------------------


Get SIG Zscaler tunnels from device

.. code:: python

    def get(device_id: str) -> Any: ...


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
        client.device.sig.zscaler.tunnels.get()


