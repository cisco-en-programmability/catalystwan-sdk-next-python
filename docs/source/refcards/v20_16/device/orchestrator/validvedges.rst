===============================
device.orchestrator.validvedges
===============================


Operation: GET /dataservice/device/orchestrator/validvedges
-----------------------------------------------------------


Get valid device list from device

.. code:: python

    def create_valid_devices_list(device_id: str) -> Any: ...


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
        client.device.orchestrator.validvedges.create_valid_devices_list()


