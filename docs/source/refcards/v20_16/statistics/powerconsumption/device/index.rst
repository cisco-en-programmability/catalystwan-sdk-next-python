==================================
statistics.powerconsumption.device
==================================


Operation: POST /dataservice/statistics/powerconsumption/device
---------------------------------------------------------------


Get Power Consumption Per Device stats

.. code:: python

    def get_power_consumption_device(
        payload: Optional[Any] = None,
    ) -> PowerConsumptionDeviceResp: ...


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
        client.statistics.powerconsumption.device.get_power_consumption_device()


.. toctree::
    :maxdepth: 1

    models

