===========================
device.sig.tunnel_dashboard
===========================


Operation: GET /dataservice/device/sig/tunnelDashboard
------------------------------------------------------


Get SIG Zscaler tunnels from device

.. code:: python

    def get() -> Any: ...


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
        client.device.sig.tunnel_dashboard.get()


