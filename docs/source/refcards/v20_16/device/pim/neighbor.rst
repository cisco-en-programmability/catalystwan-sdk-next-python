===================
device.pim.neighbor
===================


Operation: GET /dataservice/device/pim/neighbor
-----------------------------------------------


Get PIM neighbor list from device

.. code:: python

    def create_pim_neighbor_list(device_id: str) -> List[Any]: ...


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
        client.device.pim.neighbor.create_pim_neighbor_list()


