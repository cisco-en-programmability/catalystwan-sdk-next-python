==================
statistics.process
==================


Operation: GET /dataservice/statistics/process
----------------------------------------------


Process stats data

.. code:: python

    def get() -> Any: ...


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
        client.statistics.process.get()


.. toctree::
    :maxdepth: 1

    counters
    status
    thread/index

