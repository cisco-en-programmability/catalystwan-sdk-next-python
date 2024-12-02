==========================
device.cellular.connection
==========================


Operation: GET /dataservice/device/cellular/connection
------------------------------------------------------


Get cellular connection list from device

.. code:: python

    def create_cellular_connection_list(device_id: str) -> List[Any]: ...


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
        client.device.cellular.connection.create_cellular_connection_list()


