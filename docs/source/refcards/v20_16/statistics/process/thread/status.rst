================================
statistics.process.thread.status
================================


Operation: GET /dataservice/statistics/process/thread/status
------------------------------------------------------------


Get stats process thread report

.. code:: python

    def generate_stats_process_thread_report() -> List[Any]: ...


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
        client.statistics.process.thread.status.generate_stats_process_thread_report()


