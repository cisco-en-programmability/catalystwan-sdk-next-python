=======================
device.powerconsumption
=======================


Operation: GET /dataservice/device/powerconsumption
---------------------------------------------------


Get Power Consumption Information

.. code:: python

    def get_power_consumption(
        device_id: DeviceIp,
    ) -> PowerConsumptionRealTime: ...


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
        client.device.powerconsumption.get_power_consumption()


.. toctree::
    :maxdepth: 1

    models

