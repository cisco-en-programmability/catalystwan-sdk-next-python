====================
device.interface.vpn
====================


Operation: GET /dataservice/device/interface/vpn
------------------------------------------------


Get device interfaces per VPN

.. code:: python

    def generate_device_interface_vpn(device_id: str) -> Any: ...


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
        client.device.interface.vpn.generate_device_interface_vpn()


