======================================================
v2.data.device.statistics.interfacestatistics.doccount
======================================================


Operation: GET /dataservice/v2/data/device/statistics/interfacestatistics/doccount
----------------------------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_with_interface_statistics(
        start_date: str, end_date: str, time_zone: Optional[str] = None
    ) -> DocCountRes: ...


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
        client.v2.data.device.statistics.interfacestatistics.doccount.get_count_with_interface_statistics()


.. toctree::
    :maxdepth: 1

    models

