======================================
device.action.firmware_upgrade.devices
======================================


Operation: GET /dataservice/device/action/firmware-upgrade/devices
------------------------------------------------------------------


firmware supported devices

.. code:: python

    def get_firmware_devices() -> ProcessGetFirmwareRemoteImageReq: ...


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
        client.device.action.firmware_upgrade.devices.get_firmware_devices()


.. toctree::
    :maxdepth: 1

    models

