==================
statistics.dpi.csv
==================


Operation: GET /dataservice/statistics/dpi/csv
----------------------------------------------


Get raw data with optional query as CSV

.. code:: python

    def get_dpi_stats_raw_data_as_csv(
        query: Optional[str] = None,
    ) -> str: ...


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
        client.statistics.dpi.csv.get_dpi_stats_raw_data_as_csv()


