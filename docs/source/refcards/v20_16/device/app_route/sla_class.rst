==========================
device.app_route.sla_class
==========================


Operation: GET /dataservice/device/app-route/sla-class
------------------------------------------------------


Get SLA class list from device (Real Time)

.. code:: python

    def create_app_route_sla_class_list(device_id: str) -> Any: ...


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
        client.device.app_route.sla_class.create_app_route_sla_class_list()


