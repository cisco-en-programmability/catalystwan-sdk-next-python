=================
device.bridge.mac
=================


Operation: GET /dataservice/device/bridge/mac
---------------------------------------------


Get device bridge interface MAC (Real Time)

.. code:: python

    def get_bridge_interface_mac(
        device_id: str,
        bridge_id: Optional[str] = None,
        if_name: Optional[IfNameParam] = None,
        mac_address: Optional[str] = None,
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
        client.device.bridge.mac.get_bridge_interface_mac()


.. toctree::
    :maxdepth: 1

    models

