================================
statistics.system.stats.doccount
================================


Operation: GET /dataservice/statistics/system/stats/doccount
------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_17(query: str) -> Any: ...


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
        client.statistics.system.stats.doccount.get_count_17()


Operation: POST /dataservice/statistics/system/stats/doccount
-------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_18(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.system.stats.doccount.get_count_post_18()


