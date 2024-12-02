====================
device.ospf.neighbor
====================


Operation: GET /dataservice/device/ospf/neighbor
------------------------------------------------


Get OSPF neighbor list from device (Real Time)

.. code:: python

    def create_ospf_neighbors(device_id: str) -> List[Any]: ...


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
        client.device.ospf.neighbor.create_ospf_neighbors()


