==================================
device.hardware.synced.environment
==================================


Operation: GET /dataservice/device/hardware/synced/environment
--------------------------------------------------------------


Get hardware environment list synchronously from device

.. code:: python

    def create_synced_environment_list(device_id: str) -> Any: ...


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
        client.device.hardware.synced.environment.create_synced_environment_list()


