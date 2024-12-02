=============================
template.device.config.config
=============================


Operation: POST /dataservice/template/device/config/config
----------------------------------------------------------


Get device configuration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_device_configuration_preview(
        payload: Optional[Any] = None,
    ) -> str: ...


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
        client.template.device.config.config.get_device_configuration_preview()


