=======================
device.dhcpv6.interface
=======================


Operation: GET /dataservice/device/dhcpv6/interface
---------------------------------------------------


Get DHCPv6 interfaces from device

.. code:: python

    def get_dhc_pv6_interface(device_id: str) -> Any: ...


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
        client.device.dhcpv6.interface.get_dhc_pv6_interface()


