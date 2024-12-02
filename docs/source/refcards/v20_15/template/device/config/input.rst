============================
template.device.config.input
============================


Operation: POST /dataservice/template/device/config/input
---------------------------------------------------------


Create device input<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def create_device_input(payload: Optional[Any] = None) -> Any: ...


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
        client.template.device.config.input.create_device_input()


