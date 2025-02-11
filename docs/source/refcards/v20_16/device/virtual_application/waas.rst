===============================
device.virtual_application.waas
===============================


Operation: GET /dataservice/device/virtualApplication/waas
----------------------------------------------------------


Get Waas apps list from device

.. code:: python

    def create_waas_list(device_id: str) -> Any: ...


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
        client.device.virtual_application.waas.create_waas_list()


