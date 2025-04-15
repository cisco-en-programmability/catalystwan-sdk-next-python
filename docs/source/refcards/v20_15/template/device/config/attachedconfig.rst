=====================================
template.device.config.attachedconfig
=====================================


Operation: GET /dataservice/template/device/config/attachedconfig
-----------------------------------------------------------------


Get attached config to device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get(device_id: str, policy_id: Optional[str] = None) -> Any: ...


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
        client.template.device.config.attachedconfig.get()


