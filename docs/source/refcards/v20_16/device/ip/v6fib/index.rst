===============
device.ip.v6fib
===============


Operation: GET /dataservice/device/ip/v6fib
-------------------------------------------


Get IPv6 FIB list from device (Real Time)

.. code:: python

    def create_i_pv6_fib_list(
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
        client.device.ip.v6fib.create_i_pv6_fib_list()


.. toctree::
    :maxdepth: 1

    models

