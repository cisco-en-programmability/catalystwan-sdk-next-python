=======================
statistics.dpi.doccount
=======================


Operation: GET /dataservice/statistics/dpi/doccount
---------------------------------------------------


Get response count of a query

.. code:: python

    def get_dpi_stats_count(
        query: Optional[str] = None,
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
        client.statistics.dpi.doccount.get_dpi_stats_count()


Operation: POST /dataservice/statistics/dpi/doccount
----------------------------------------------------


Get response count of a query

.. code:: python

    def get_dpi_stats_count_post(
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
        client.statistics.dpi.doccount.get_dpi_stats_count_post()


.. toctree::
    :maxdepth: 1

    models

