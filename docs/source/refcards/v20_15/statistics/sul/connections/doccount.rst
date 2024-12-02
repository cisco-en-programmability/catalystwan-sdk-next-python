===================================
statistics.sul.connections.doccount
===================================


Operation: GET /dataservice/statistics/sul/connections/doccount
---------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_14(query: str) -> Any: ...


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
        client.statistics.sul.connections.doccount.get_count_14()


Operation: POST /dataservice/statistics/sul/connections/doccount
----------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_14(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.sul.connections.doccount.get_count_post_14()


