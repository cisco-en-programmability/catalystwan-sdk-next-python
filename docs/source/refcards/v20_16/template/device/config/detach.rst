=============================
template.device.config.detach
=============================


Operation: POST /dataservice/template/device/config/detach
----------------------------------------------------------


Deprecated!!!

Detach device template<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def detach_device_template(payload: Optional[Any] = None) -> None: ...


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
        client.template.device.config.detach.detach_device_template()


