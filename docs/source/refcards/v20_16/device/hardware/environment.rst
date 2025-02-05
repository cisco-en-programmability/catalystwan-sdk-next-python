===========================
device.hardware.environment
===========================


Operation: GET /dataservice/device/hardware/environment
-------------------------------------------------------


Get hardware environment list from device

.. code:: python

    def create_environment_list(device_id: str) -> Any: ...


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
        client.device.hardware.environment.create_environment_list()


