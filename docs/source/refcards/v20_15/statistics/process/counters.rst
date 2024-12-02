===========================
statistics.process.counters
===========================


Operation: GET /dataservice/statistics/process/counters
-------------------------------------------------------


Get statistics processing counters

.. code:: python

    def get_statistics_processing_counters() -> List[Any]: ...


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
        client.statistics.process.counters.get_statistics_processing_counters()


