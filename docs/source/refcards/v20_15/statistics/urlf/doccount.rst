========================
statistics.urlf.doccount
========================


Operation: GET /dataservice/statistics/urlf/doccount
----------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_22(query: str) -> Any: ...


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
        client.statistics.urlf.doccount.get_count_22()


Operation: POST /dataservice/statistics/urlf/doccount
-----------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_22(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.urlf.doccount.get_count_post_22()


