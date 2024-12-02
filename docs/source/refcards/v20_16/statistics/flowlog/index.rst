==================
statistics.flowlog
==================


Operation: GET /dataservice/statistics/flowlog
----------------------------------------------


Get stats raw data

.. code:: python

    def get_stat_data_raw_data_14(
        query: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        site_id: Optional[str] = None,
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
        client.statistics.flowlog.get_stat_data_raw_data_14()


Operation: POST /dataservice/statistics/flowlog
-----------------------------------------------


Get stats raw data

.. code:: python

    def get_stat_data_raw_data_post(
        payload: Optional[Any] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[SortOrderParam] = None,
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
        client.statistics.flowlog.get_stat_data_raw_data_post()


.. toctree::
    :maxdepth: 1

    aggregation/index
    csv
    doccount/index
    fields/index
    page/index
    query/index
    models

