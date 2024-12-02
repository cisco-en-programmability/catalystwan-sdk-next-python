==========
device.arp
==========


Operation: GET /dataservice/device/arp
--------------------------------------


Get ARP interfaces from device (Real Time)

.. code:: python

    def get_arp_interface(device_id: str) -> Any: ...


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
        client.device.arp.get_arp_interface()


