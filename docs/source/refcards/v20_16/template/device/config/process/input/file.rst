=========================================
template.device.config.process.input.file
=========================================


Operation: POST /dataservice/template/device/config/process/input/file
----------------------------------------------------------------------


Process input comma separated file<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def post(payload: Any) -> str: ...


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
        client.template.device.config.process.input.file.post()


