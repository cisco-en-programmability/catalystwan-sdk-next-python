========================
device.csp.system.native
========================


Operation: GET /dataservice/device/csp/system/native
----------------------------------------------------


Get device system native settings from device

.. code:: python

    def create_device_system_setting_native_info(
        device_id: str,
    ) -> Any: ...


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
        client.device.csp.system.native.create_device_system_setting_native_info()


