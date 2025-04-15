====================
device.tools.netstat
====================


Operation: GET /dataservice/device/tools/netstat
------------------------------------------------


Get device tool net stat

.. code:: python

    def get(
        device_id: str,
        vpn: Optional[VpnParam] = None,
        options: Optional[str] = None,
    ) -> Any: ...


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
        client.device.tools.netstat.get()


.. toctree::
    :maxdepth: 1

    models

