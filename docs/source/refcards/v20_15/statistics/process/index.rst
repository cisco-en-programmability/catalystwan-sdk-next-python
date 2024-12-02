==================
statistics.process
==================


Operation: GET /dataservice/statistics/process
----------------------------------------------


Process stats data

.. code:: python

    def process_statistics_data() -> Any: ...


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
        client.statistics.process.process_statistics_data()


.. toctree::
    :maxdepth: 1

    counters
    status
    thread/index

