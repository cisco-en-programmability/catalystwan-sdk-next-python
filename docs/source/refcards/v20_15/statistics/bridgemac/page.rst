=========================
statistics.bridgemac.page
=========================


Operation: GET /dataservice/statistics/bridgemac/page
-----------------------------------------------------


Get stats raw data

.. code:: python

    def get_stats_pagination_raw_data_5(
        query: Optional[str] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
    ) -> Any: ...


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
        client.statistics.bridgemac.page.get_stats_pagination_raw_data_5()


Operation: POST /dataservice/statistics/bridgemac/page
------------------------------------------------------


Get stats raw data

.. code:: python

    def get_post_stats_pagination_raw_data_5(
        payload: Optional[Any] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
    ) -> Any: ...


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
        client.statistics.bridgemac.page.get_post_stats_pagination_raw_data_5()


