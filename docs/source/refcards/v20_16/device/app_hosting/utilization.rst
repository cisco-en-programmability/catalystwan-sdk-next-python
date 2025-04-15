==============================
device.app_hosting.utilization
==============================


Operation: GET /dataservice/device/app-hosting/utilization
----------------------------------------------------------


Get App hosting utilization from device

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
        client.device.app_hosting.utilization.get()


