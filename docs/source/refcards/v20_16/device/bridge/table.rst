===================
device.bridge.table
===================


Operation: GET /dataservice/device/bridge/table
-----------------------------------------------


Get device bridge interface table (Real Time)

.. code:: python

    def get_bridge_interface_table(device_id: str) -> Any: ...


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
        client.device.bridge.table.get_bridge_interface_table()


