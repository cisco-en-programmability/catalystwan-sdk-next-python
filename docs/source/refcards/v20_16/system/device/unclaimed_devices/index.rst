===============================
system.device.unclaimed_devices
===============================


Operation: GET /dataservice/system/device/unclaimedDevices
----------------------------------------------------------


Get list of all unclaimed devices

.. code:: python

    def get_all_unclaimed_devices() -> GetAllUnclaimedDevices: ...


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
        client.system.device.unclaimed_devices.get_all_unclaimed_devices()


.. toctree::
    :maxdepth: 1

    models

