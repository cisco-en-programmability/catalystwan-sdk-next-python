========================
device.dpi.device.fields
========================


Operation: GET /dataservice/device/dpi/device/fields
----------------------------------------------------


Get DPI field from device

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
        client.device.dpi.device.fields.get()


