===================================
template.device.config.attachcloudx
===================================


Operation: PUT /dataservice/template/device/config/attachcloudx
---------------------------------------------------------------


Edit already enabled gateways, clients, dias<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def edit_cloudx_config(payload: Optional[Any] = None) -> str: ...


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
        client.template.device.config.attachcloudx.edit_cloudx_config()


Operation: POST /dataservice/template/device/config/attachcloudx
----------------------------------------------------------------


Enable gateways, clients, dias

.. code:: python

    def push_cloudx_config(payload: Optional[Any] = None) -> str: ...


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
        client.template.device.config.attachcloudx.push_cloudx_config()


