============================
template.device.config.vbond
============================


Operation: GET /dataservice/template/device/config/vbond
--------------------------------------------------------


Check if vBond is configured<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

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
        client.template.device.config.vbond.get()


