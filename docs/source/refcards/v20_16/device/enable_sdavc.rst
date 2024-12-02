===================
device.enable_sdavc
===================


Operation: POST /dataservice/device/enableSDAVC/{deviceIP}/{enable}
-------------------------------------------------------------------


Enable/Disable SDAVC on device

.. code:: python

    def enable_sdavc_on_device(device_ip: str, enable: bool) -> None: ...


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
        client.device.enable_sdavc.enable_sdavc_on_device()


