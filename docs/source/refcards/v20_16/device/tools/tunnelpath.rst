=======================
device.tools.tunnelpath
=======================


Operation: POST /dataservice/device/tools/tunnelpath/{deviceIP}
---------------------------------------------------------------


TunnelPath

.. code:: python

    def tunnel_path(
        device_ip: str, payload: Optional[Any] = None
    ) -> None: ...


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
        client.device.tools.tunnelpath.tunnel_path()


