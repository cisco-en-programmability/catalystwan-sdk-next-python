====================
statistics.interface
====================


Operation: GET /dataservice/statistics/interface
------------------------------------------------


Get stats raw data

.. code:: python

    def get_stat_data_raw_data_11(
        query: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[SortOrderParam] = None,
    ) -> InterfaceQuery: ...


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
        client.statistics.interface.get_stat_data_raw_data_11()


Operation: POST /dataservice/statistics/interface
-------------------------------------------------


Get stats raw data

.. code:: python

    def get_stats_raw_data_11(
        payload: Optional[Any] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[SortOrderParam] = None,
    ) -> List[InterfaceRespWithPageInfo]: ...


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
        client.statistics.interface.get_stats_raw_data_11()


.. toctree::
    :maxdepth: 1

    aggregation/index
    app_agg/index
    ccapacity/index
    csv
    doccount
    fields/index
    page/index
    query/index
    type_/index
    models

