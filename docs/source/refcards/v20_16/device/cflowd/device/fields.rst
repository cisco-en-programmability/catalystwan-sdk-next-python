===========================
device.cflowd.device.fields
===========================


Operation: GET /dataservice/device/cflowd/device/fields
-------------------------------------------------------


Get CflowdvDPI query field JSON

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
        client.device.cflowd.device.fields.get()


