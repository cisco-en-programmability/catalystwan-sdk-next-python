==============================
statistics.apphosting.doccount
==============================


Operation: GET /dataservice/statistics/apphosting/doccount
----------------------------------------------------------


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
        client.statistics.apphosting.doccount.get_count_3()


Operation: POST /dataservice/statistics/apphosting/doccount
-----------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_2(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.apphosting.doccount.get_count_post_2()


