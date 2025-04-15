========================================
device.tools.admintech.supportedfeatures
========================================


Operation: GET /dataservice/device/tools/admintech/supportedfeatures/{deviceModel}/{deviceIP}/{personality}
-----------------------------------------------------------------------------------------------------------


Get supported admin tech features

.. code:: python

    def get(
        device_model: DeviceModel, device_ip: DeviceIp, personality: str
    ) -> None: ...


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
        client.device.tools.admintech.supportedfeatures.get()


.. toctree::
    :maxdepth: 1

    models

