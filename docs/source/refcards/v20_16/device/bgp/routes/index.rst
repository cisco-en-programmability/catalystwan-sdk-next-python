=================
device.bgp.routes
=================


Operation: GET /dataservice/device/bgp/routes
---------------------------------------------


Get BGP routes list (Real Time)

.. code:: python

    def create_bgp_routes_list(
        device_id: str,
        vpn_id: Optional[VpnIdParam] = None,
        prefix: Optional[str] = None,
        nexthop: Optional[str] = None,
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
        client.device.bgp.routes.create_bgp_routes_list()


.. toctree::
    :maxdepth: 1

    models

