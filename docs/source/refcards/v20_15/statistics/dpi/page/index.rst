===================
statistics.dpi.page
===================


Operation: GET /dataservice/statistics/dpi/page
-----------------------------------------------


Get DPI stats pagination raw data

.. code:: python

    def get_dpi_stats_pagination_raw_data(
        query: Optional[str] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
    ) -> DpiPaginationResponse: ...


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
        client.statistics.dpi.page.get_dpi_stats_pagination_raw_data()


Operation: POST /dataservice/statistics/dpi/page
------------------------------------------------


Get DPI stats pagination raw data

.. code:: python

    def get_dpi_stats_pagination_raw_data_post(
        payload: Optional[Any] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
    ) -> DpiPaginationResponse: ...


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
        client.statistics.dpi.page.get_dpi_stats_pagination_raw_data_post()


.. toctree::
    :maxdepth: 1

    models

