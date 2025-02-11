==========================
statistics.cflowd.doccount
==========================


Operation: GET /dataservice/statistics/cflowd/doccount
------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_9(query: str) -> Any: ...


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
        client.statistics.cflowd.doccount.get_count_9()


Operation: POST /dataservice/statistics/cflowd/doccount
-------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_9(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.cflowd.doccount.get_count_post_9()


