==========================================
device.bfd.state.device.tloc_interface_map
==========================================


Operation: GET /dataservice/device/bfd/state/device/tlocInterfaceMap
--------------------------------------------------------------------


Get device tloc color to Intf Mapping Relationship

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
        client.device.bfd.state.device.tloc_interface_map.get()


