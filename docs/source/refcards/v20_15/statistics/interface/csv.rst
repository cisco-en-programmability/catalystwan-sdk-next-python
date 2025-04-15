========================
statistics.interface.csv
========================


Operation: GET /dataservice/statistics/interface/csv
----------------------------------------------------


Get raw data with optional query as CSV

.. code:: python

    def get(query: str) -> str: ...


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
        client.statistics.interface.csv.get()


