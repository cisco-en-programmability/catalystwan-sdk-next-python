============================
statistics.approute.doccount
============================


Operation: GET /dataservice/statistics/approute/doccount
--------------------------------------------------------


Get response count of a query

.. code:: python

    def get_doc_count_1(query: str) -> Any: ...


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
        client.statistics.approute.doccount.get_doc_count_1()


Operation: POST /dataservice/statistics/approute/doccount
---------------------------------------------------------


Get response count of a query

.. code:: python

    def get_doc_count_post(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.approute.doccount.get_doc_count_post()


