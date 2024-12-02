===============================
device.appqoe.flow_closed_error
===============================


Operation: GET /dataservice/device/appqoe/flow-closed-error
-----------------------------------------------------------


Get Appqoe flow closed error from device

.. code:: python

    def get_appqoe_flow_closed_error(device_id: str) -> Any: ...


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
        client.device.appqoe.flow_closed_error.get_appqoe_flow_closed_error()


