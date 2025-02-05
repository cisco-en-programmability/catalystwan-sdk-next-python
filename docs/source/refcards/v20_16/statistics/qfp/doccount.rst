=======================
statistics.qfp.doccount
=======================


Operation: GET /dataservice/statistics/qfp/doccount
---------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_3(query: str) -> Any: ...


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
        client.statistics.qfp.doccount.get_count_3()


Operation: POST /dataservice/statistics/qfp/doccount
----------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_3(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.qfp.doccount.get_count_post_3()


