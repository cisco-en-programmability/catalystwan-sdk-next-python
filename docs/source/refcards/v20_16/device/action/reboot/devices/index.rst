============================
device.action.reboot.devices
============================


Operation: GET /dataservice/device/action/reboot/devices/{deviceType}
---------------------------------------------------------------------


Get list of rebooted devices

.. code:: python

    def get(
        device_type: str, group_id: str
    ) -> GenerateRebootDeviceList: ...


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
        client.device.action.reboot.devices.get()


.. toctree::
    :maxdepth: 1

    models

