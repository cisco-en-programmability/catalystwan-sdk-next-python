===========================================
template.device.config.quickconnectvariable
===========================================


Operation: POST /dataservice/template/device/config/quickconnectvariable
------------------------------------------------------------------------


Get connection variables to be configured

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
        client.template.device.config.quickconnectvariable.post()


