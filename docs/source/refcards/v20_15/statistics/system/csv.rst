=====================
statistics.system.csv
=====================


Operation: GET /dataservice/statistics/system/csv
-------------------------------------------------


Get raw data with optional query as CSV

.. code:: python

    def get_stat_data_raw_data_as_csv_16(
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
        client.statistics.system.csv.get_stat_data_raw_data_as_csv_16()


