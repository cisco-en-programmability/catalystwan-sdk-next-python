======================
statistics.flowlog.csv
======================


Operation: GET /dataservice/statistics/flowlog/csv
--------------------------------------------------


Get raw data with optional query as CSV

.. code:: python

    def get(query: Optional[str] = None) -> str: ...


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
        client.statistics.flowlog.csv.get()


