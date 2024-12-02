====================
device.appqoe.status
====================


Operation: GET /dataservice/device/appqoe/status
------------------------------------------------


Get Appqoe status from device

.. code:: python

    def get_appqoe_status(device_id: str) -> Any: ...


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
        client.device.appqoe.status.get_appqoe_status()


