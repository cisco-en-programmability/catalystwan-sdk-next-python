===========================
device.transport.connection
===========================


Operation: GET /dataservice/device/transport/connection
-------------------------------------------------------


Get transport connection list from device

.. code:: python

    def create_transport_connection_list(device_id: str) -> List[Any]: ...


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
        client.device.transport.connection.create_transport_connection_list()


