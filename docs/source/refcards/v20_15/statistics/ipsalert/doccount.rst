============================
statistics.ipsalert.doccount
============================


Operation: GET /dataservice/statistics/ipsalert/doccount
--------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_21(query: str) -> Any: ...


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
        client.statistics.ipsalert.doccount.get_count_21()


Operation: POST /dataservice/statistics/ipsalert/doccount
---------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_21(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.ipsalert.doccount.get_count_post_21()


