=============================================
v2.data.device.statistics.interfacestatistics
=============================================


Operation: GET /dataservice/v2/data/device/statistics/interfacestatistics
-------------------------------------------------------------------------


Get device statistics data

.. code:: python

    def generate_device_interface_statistics_data(
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
        time_zone: Optional[str] = None,
    ) -> List[InterfaceStatisticsRes]: ...


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
        client.v2.data.device.statistics.interfacestatistics.generate_device_interface_statistics_data()


.. toctree::
    :maxdepth: 1

    doccount/index
    fields/index
    models

