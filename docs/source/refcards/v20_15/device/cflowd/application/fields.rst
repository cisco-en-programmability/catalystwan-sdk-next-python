================================
device.cflowd.application.fields
================================


Operation: GET /dataservice/device/cflowd/application/fields
------------------------------------------------------------


Get Cflowd DPI query field JSON

.. code:: python

    def get_cflowd_dpi_device_field_json(
        is_device_dash_board: Optional[bool] = False,
    ) -> Any: ...


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
        client.device.cflowd.application.fields.get_cflowd_dpi_device_field_json()


