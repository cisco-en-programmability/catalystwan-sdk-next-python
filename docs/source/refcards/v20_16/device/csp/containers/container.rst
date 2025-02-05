===============================
device.csp.containers.container
===============================


Operation: GET /dataservice/device/csp/containers/container
-----------------------------------------------------------


Get device container from device (Real Time)

.. code:: python

    def create_device_containers_info(device_id: str) -> Any: ...


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
        client.device.csp.containers.container.create_device_containers_info()


