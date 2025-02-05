===================================
template.device.config.detachcloudx
===================================


Operation: POST /dataservice/template/device/config/detachcloudx
----------------------------------------------------------------


Disable enabled gateways, clients, dias<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def detach_sites(payload: Optional[Any] = None) -> str: ...


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
        client.template.device.config.detachcloudx.detach_sites()


