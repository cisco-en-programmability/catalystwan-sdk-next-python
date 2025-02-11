======================
device.cflowd.template
======================


Operation: GET /dataservice/device/cflowd/template
--------------------------------------------------


Get cflowd template from device

.. code:: python

    def create_cflowd_template(device_id: str) -> Any: ...


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
        client.device.cflowd.template.create_cflowd_template()


