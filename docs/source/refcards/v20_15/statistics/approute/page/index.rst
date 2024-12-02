========================
statistics.approute.page
========================


Operation: GET /dataservice/statistics/approute/page
----------------------------------------------------


Get stats raw data

.. code:: python

    def get_stat_bulk_raw_data(
        query: Optional[str] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
    ) -> AppRouteAggRespWithPageInfo: ...


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
        client.statistics.approute.page.get_stat_bulk_raw_data()


Operation: POST /dataservice/statistics/approute/page
-----------------------------------------------------


Get stats raw data

.. code:: python

    def get_post_stat_bulk_raw_data(
        payload: Optional[Any] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
    ) -> AppRouteAggRespWithPageInfo: ...


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
        client.statistics.approute.page.get_post_stat_bulk_raw_data()


.. toctree::
    :maxdepth: 1

    models

