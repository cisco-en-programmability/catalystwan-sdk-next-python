==================
device.eigrp.route
==================


Operation: GET /dataservice/device/eigrp/route
----------------------------------------------


Get EIGRP route from device (Real Time)

.. code:: python

    def create_eigrp_route(device_id: str) -> Any: ...


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
        client.device.eigrp.route.create_eigrp_route()


