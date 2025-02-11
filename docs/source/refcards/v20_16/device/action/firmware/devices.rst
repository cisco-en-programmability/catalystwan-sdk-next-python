==============================
device.action.firmware.devices
==============================


Operation: GET /dataservice/device/action/firmware/devices
----------------------------------------------------------


Deprecated!!!

Get list of devices that support firmware upgrade

.. code:: python

    def get_devices_fw_upgrade() -> None: ...


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
        client.device.action.firmware.devices.get_devices_fw_upgrade()


