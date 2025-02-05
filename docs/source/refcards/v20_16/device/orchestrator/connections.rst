===============================
device.orchestrator.connections
===============================


Operation: GET /dataservice/device/orchestrator/connections
-----------------------------------------------------------


Get connection list from device

.. code:: python

    def create_connection_list_from_device(device_id: str) -> Any: ...


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
        client.device.orchestrator.connections.create_connection_list_from_device()


