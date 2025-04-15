==============================
device.dpi.application_mapping
==============================


Operation: GET /dataservice/device/dpi/application-mapping
----------------------------------------------------------


Get DPI supported application list from device

.. code:: python

    def get() -> List[Any]: ...


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
        client.device.dpi.application_mapping.get()


