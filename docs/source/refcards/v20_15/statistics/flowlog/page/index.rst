=======================
statistics.flowlog.page
=======================


Operation: GET /dataservice/statistics/flowlog/page
---------------------------------------------------


Get stats pagination raw data

.. code:: python

    def get_stats_pagination_raw_data_23(
        query: Optional[str] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
    ) -> FlowlogPaginationResponse: ...


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
        client.statistics.flowlog.page.get_stats_pagination_raw_data_23()


Operation: POST /dataservice/statistics/flowlog/page
----------------------------------------------------


Get stats pagination raw data

.. code:: python

    def get_stats_pagination_raw_data_post(
        payload: Optional[Any] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
    ) -> FlowlogPaginationResponse: ...


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
        client.statistics.flowlog.page.get_stats_pagination_raw_data_post()


.. toctree::
    :maxdepth: 1

    models

