=========================
statistics.fwall.doccount
=========================


Operation: GET /dataservice/statistics/fwall/doccount
-----------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_23(query: str) -> Any: ...


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
        client.statistics.fwall.doccount.get_count_23()


Operation: POST /dataservice/statistics/fwall/doccount
------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_24(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.fwall.doccount.get_count_post_24()


