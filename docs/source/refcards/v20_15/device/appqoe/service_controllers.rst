=================================
device.appqoe.service_controllers
=================================


Operation: GET /dataservice/device/appqoe/service-controllers
-------------------------------------------------------------


Get Appqoe service controllers from device

.. code:: python

    def get_appqoe_service_controllers(device_id: str) -> Any: ...


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
        client.device.appqoe.service_controllers.get_appqoe_service_controllers()


