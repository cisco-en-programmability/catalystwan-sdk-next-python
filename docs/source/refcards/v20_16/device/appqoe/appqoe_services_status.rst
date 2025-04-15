====================================
device.appqoe.appqoe_services_status
====================================


Operation: GET /dataservice/device/appqoe/appqoe-services-status
----------------------------------------------------------------


Get Appqoe Services Status from device

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
        client.device.appqoe.appqoe_services_status.get()


