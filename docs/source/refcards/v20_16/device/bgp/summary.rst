==================
device.bgp.summary
==================


Operation: GET /dataservice/device/bgp/summary
----------------------------------------------


Get BGP summary (Real Time)

.. code:: python

    def get(device_id: str) -> Any: ...


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
        client.device.bgp.summary.get()


