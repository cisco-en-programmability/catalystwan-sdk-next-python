====================
device.ip.routetable
====================


Operation: GET /dataservice/device/ip/routetable
------------------------------------------------


Get route table list from device (Real Time)

.. code:: python

    def get(
        device_id: str,
        vpn_id: Optional[VpnIdParam] = None,
        address_family: Optional[AddressFamilyParam] = None,
        prefix: Optional[str] = None,
        protocol: Optional[str] = None,
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
        client.device.ip.routetable.get()


.. toctree::
    :maxdepth: 1

    models

