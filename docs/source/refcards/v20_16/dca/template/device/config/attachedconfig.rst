=========================================
dca.template.device.config.attachedconfig
=========================================


Operation: POST /dataservice/dca/template/device/config/attachedconfig
----------------------------------------------------------------------


Get attached config to device

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.dca.template.device.config.attachedconfig.post()


