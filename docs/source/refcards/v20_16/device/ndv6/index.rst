===========
device.ndv6
===========


Operation: GET /dataservice/device/ndv6
---------------------------------------


Get IPv6 Neighbors from device (Real Time)

.. code:: python

    def get(
        device_id: str,
        vpn_id: Optional[VpnIdParam] = None,
        if_name: Optional[IfNameParam] = None,
        mac: Optional[str] = None,
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
        client.device.ndv6.get()


.. toctree::
    :maxdepth: 1

    models

