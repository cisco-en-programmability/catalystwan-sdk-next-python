=======================
device.cellular.network
=======================


Operation: GET /dataservice/device/cellular/network
---------------------------------------------------


Get cellular network list from device

.. code:: python

    def create_network_list(device_id: str) -> List[Any]: ...


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
        client.device.cellular.network.create_network_list()


