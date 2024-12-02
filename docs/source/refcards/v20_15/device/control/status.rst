=====================
device.control.status
=====================


Operation: GET /dataservice/device/control/status
-------------------------------------------------


Get local device status

.. code:: python

    def get_local_device_status() -> Any: ...


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
        client.device.control.status.get_local_device_status()


