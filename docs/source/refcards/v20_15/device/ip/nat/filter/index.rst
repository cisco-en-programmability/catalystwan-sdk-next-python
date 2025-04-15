====================
device.ip.nat.filter
====================


Operation: GET /dataservice/device/ip/nat/filter
------------------------------------------------


Get NAT filter list from device

.. code:: python

    def get(
        device_id: str,
        nat_vpn_id: Optional[str] = None,
        nat_ifname: Optional[str] = None,
        private_source_address: Optional[str] = None,
        proto: Optional[ProtoParam] = None,
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
        client.device.ip.nat.filter.get()


.. toctree::
    :maxdepth: 1

    models

