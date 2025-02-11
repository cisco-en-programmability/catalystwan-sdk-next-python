=======================
device.bridge.interface
=======================


Operation: GET /dataservice/device/bridge/interface
---------------------------------------------------


Get device bridge interface list (Real Time)

.. code:: python

    def get_bridge_interface_list(device_id: str) -> Any: ...


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
        client.device.bridge.interface.get_bridge_interface_list()


