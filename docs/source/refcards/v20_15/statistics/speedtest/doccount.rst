=============================
statistics.speedtest.doccount
=============================


Operation: GET /dataservice/statistics/speedtest/doccount
---------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_25(query: str) -> Any: ...


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
        client.statistics.speedtest.doccount.get_count_25()


Operation: POST /dataservice/statistics/speedtest/doccount
----------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_25(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.speedtest.doccount.get_count_post_25()


