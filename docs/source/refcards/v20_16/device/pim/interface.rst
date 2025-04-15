====================
device.pim.interface
====================


Operation: GET /dataservice/device/pim/interface
------------------------------------------------


Get PIM interface list from device

.. code:: python

    def get(device_id: str) -> List[Any]: ...


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
        client.device.pim.interface.get()


