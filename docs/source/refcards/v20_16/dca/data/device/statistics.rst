==========================
dca.data.device.statistics
==========================


Operation: POST /dataservice/dca/data/device/statistics/{stats_data_type}
-------------------------------------------------------------------------


Get device statistics data

.. code:: python

    def generate_dca_device_statistics_data(
        stats_data_type: str, payload: Optional[Any] = None
    ) -> Any: ...


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
        client.dca.data.device.statistics.generate_dca_device_statistics_data()


