=============================
device.action.firmware.remove
=============================


Operation: POST /dataservice/device/action/firmware/remove
----------------------------------------------------------


Deprecated!!!

Remove firmware on device

.. code:: python

    def remove_firmware_image(payload: Optional[str] = None) -> None: ...


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
        client.device.action.firmware.remove.remove_firmware_image()


