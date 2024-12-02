=============================
device.action.install.devices
=============================


Operation: GET /dataservice/device/action/install/devices/{deviceType}
----------------------------------------------------------------------


Get list of installed devices

.. code:: python

    def generate_device_list(
        device_type: str, group_id: Optional[str] = None
    ) -> GenerateDeviceList: ...


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
        client.device.action.install.devices.generate_device_list()


.. toctree::
    :maxdepth: 1

    models

