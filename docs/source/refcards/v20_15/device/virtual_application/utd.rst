==============================
device.virtual_application.utd
==============================


Operation: GET /dataservice/device/virtualApplication/utd
---------------------------------------------------------


Get Utd apps list from device

.. code:: python

    def get(device_id: str) -> Any: ...


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
        client.device.virtual_application.utd.get()


