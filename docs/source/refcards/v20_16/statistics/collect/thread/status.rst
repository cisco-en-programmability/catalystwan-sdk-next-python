================================
statistics.collect.thread.status
================================


Operation: GET /dataservice/statistics/collect/thread/status
------------------------------------------------------------


Get stats collect thread report

.. code:: python

    def get() -> List[Any]: ...


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
        client.statistics.collect.thread.status.get()


