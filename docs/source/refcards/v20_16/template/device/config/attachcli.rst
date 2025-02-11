================================
template.device.config.attachcli
================================


Operation: POST /dataservice/template/device/config/attachcli
-------------------------------------------------------------


Attach CLI device template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def push_cli_template(payload: Optional[Any] = None) -> Any: ...


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
        client.template.device.config.attachcli.push_cli_template()


