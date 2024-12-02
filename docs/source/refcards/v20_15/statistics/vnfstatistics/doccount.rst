=================================
statistics.vnfstatistics.doccount
=================================


Operation: GET /dataservice/statistics/vnfstatistics/doccount
-------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_12(query: str) -> Any: ...


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
        client.statistics.vnfstatistics.doccount.get_count_12()


Operation: POST /dataservice/statistics/vnfstatistics/doccount
--------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_12(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.vnfstatistics.doccount.get_count_post_12()


