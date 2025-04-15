===========================
statistics.collection.reset
===========================


Operation: GET /dataservice/statistics/collection/reset/{processQueue}
----------------------------------------------------------------------


Reset stats collect thread report

.. code:: python

    def get(process_queue: int) -> Any: ...


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
        client.statistics.collection.reset.get()


