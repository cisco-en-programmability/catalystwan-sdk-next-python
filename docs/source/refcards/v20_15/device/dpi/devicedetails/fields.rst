===============================
device.dpi.devicedetails.fields
===============================


Operation: GET /dataservice/device/dpi/devicedetails/fields
-----------------------------------------------------------


Get DPI detailed field from device

.. code:: python

    def get() -> Any: ...


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
        client.device.dpi.devicedetails.fields.get()


