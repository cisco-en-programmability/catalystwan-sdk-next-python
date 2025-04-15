====================
device.bgp.neighbors
====================


Operation: GET /dataservice/device/bgp/neighbors
------------------------------------------------


Get BGP neighbors list (Real Time)

.. code:: python

    def get(
        device_id: str,
        vpn_id: Optional[VpnIdParam] = None,
        peer_addr: Optional[str] = None,
        as_: Optional[str] = None,
    ) -> List[Any]: ...


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
        client.device.bgp.neighbors.get()


.. toctree::
    :maxdepth: 1

    models

