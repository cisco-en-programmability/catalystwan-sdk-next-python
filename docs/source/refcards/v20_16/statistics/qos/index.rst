==============
statistics.qos
==============


Operation: GET /dataservice/statistics/qos
------------------------------------------


Get stats raw data

.. code:: python

    def get_stat_data_raw_data_13(
        query: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[SortOrderParam] = None,
    ) -> List[QoSRespWithPageInfo]: ...


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
        client.statistics.qos.get_stat_data_raw_data_13()


Operation: POST /dataservice/statistics/qos
-------------------------------------------


Get stats raw data

.. code:: python

    def get_stats_raw_data12(
        payload: Optional[Any] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[SortOrderParam] = None,
    ) -> List[QoSRespWithPageInfo]: ...


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
        client.statistics.qos.get_stats_raw_data12()


.. toctree::
    :maxdepth: 1

    aggregation/index
    app_agg/index
    csv
    doccount
    fields
    page/index
    query/index
    models

