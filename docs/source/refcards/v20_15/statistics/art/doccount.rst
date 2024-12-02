=======================
statistics.art.doccount
=======================


Operation: GET /dataservice/statistics/art/doccount
---------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_5(query: str) -> Any: ...


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
        client.statistics.art.doccount.get_count_5()


Operation: POST /dataservice/statistics/art/doccount
----------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_4(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.art.doccount.get_count_post_4()


