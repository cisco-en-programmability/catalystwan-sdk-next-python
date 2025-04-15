===============
device.ip.v4fib
===============


Operation: GET /dataservice/device/ip/v4fib
-------------------------------------------


Get IPv4 FIB list from device (Real Time)

.. code:: python

    def get(
        device_id: str,
        vpn_id: Optional[VpnIdParam] = None,
        prefix: Optional[str] = None,
        tloc: Optional[str] = None,
        color: Optional[ColorParam] = None,
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
        client.device.ip.v4fib.get()


.. toctree::
    :maxdepth: 1

    models

