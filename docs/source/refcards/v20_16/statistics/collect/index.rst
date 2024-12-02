==================
statistics.collect
==================


Operation: GET /dataservice/statistics/collect
----------------------------------------------


Start stats collect

.. code:: python

    def start_stats_collection() -> Any: ...


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
        client.statistics.collect.start_stats_collection()


.. toctree::
    :maxdepth: 1

    thread/index

