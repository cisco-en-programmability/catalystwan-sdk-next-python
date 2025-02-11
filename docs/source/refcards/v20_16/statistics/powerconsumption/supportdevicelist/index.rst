=============================================
statistics.powerconsumption.supportdevicelist
=============================================


Operation: GET /dataservice/statistics/powerconsumption/supportdevicelist
-------------------------------------------------------------------------


Get power consumption collection supported device list

.. code:: python

    def get_supported_device_list(
        last_n_hours: Optional[int] = 24,
    ) -> SupportedDeviceList: ...


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
        client.statistics.powerconsumption.supportdevicelist.get_supported_device_list()


.. toctree::
    :maxdepth: 1

    models

