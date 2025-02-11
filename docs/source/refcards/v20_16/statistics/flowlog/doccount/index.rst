===========================
statistics.flowlog.doccount
===========================


Operation: GET /dataservice/statistics/flowlog/doccount
-------------------------------------------------------


Get response count of a query

.. code:: python

    def get_flowlog_count(query: str) -> CountResponse: ...


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
        client.statistics.flowlog.doccount.get_flowlog_count()


Operation: POST /dataservice/statistics/flowlog/doccount
--------------------------------------------------------


Get response count of a query

.. code:: python

    def get_flowlog_count_post(
        payload: Optional[Any] = None,
    ) -> CountResponse: ...


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
        client.statistics.flowlog.doccount.get_flowlog_count_post()


.. toctree::
    :maxdepth: 1

    models

