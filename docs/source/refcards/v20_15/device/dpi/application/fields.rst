=============================
device.dpi.application.fields
=============================


Operation: GET /dataservice/device/dpi/application/fields
---------------------------------------------------------


Get DPI query field from device

.. code:: python

    def get(is_device_dash_board: Optional[bool] = False) -> Any: ...


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
        client.device.dpi.application.fields.get()


