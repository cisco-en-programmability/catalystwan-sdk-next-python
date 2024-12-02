==========
device.vpn
==========


Operation: GET /dataservice/device/vpn
--------------------------------------


Get VPN instance list from device (Real Time)

.. code:: python

    def get_vpn_instances(device_id: str) -> Any: ...


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
        client.device.vpn.get_vpn_instances()


