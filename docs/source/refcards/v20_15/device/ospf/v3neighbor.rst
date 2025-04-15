======================
device.ospf.v3neighbor
======================


Operation: GET /dataservice/device/ospf/v3neighbor
--------------------------------------------------


Get OSPF v3 neighbor list from device (Real Time)

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
        client.device.ospf.v3neighbor.get()


