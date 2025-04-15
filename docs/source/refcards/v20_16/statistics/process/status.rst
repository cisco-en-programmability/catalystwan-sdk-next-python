=========================
statistics.process.status
=========================


Operation: GET /dataservice/statistics/process/status
-----------------------------------------------------


Get stats process report

.. code:: python

    def get(process_queue: Optional[int] = None) -> List[Any]: ...


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
        client.statistics.process.status.get()


