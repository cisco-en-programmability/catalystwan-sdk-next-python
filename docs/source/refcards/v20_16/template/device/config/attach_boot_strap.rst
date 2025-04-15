========================================
template.device.config.attach_boot_strap
========================================


Operation: POST /dataservice/template/device/config/attachBootStrap
-------------------------------------------------------------------


Attach feature device template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

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
        client.template.device.config.attach_boot_strap.post()


