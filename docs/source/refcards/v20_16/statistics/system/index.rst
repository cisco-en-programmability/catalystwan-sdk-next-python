=================
statistics.system
=================


Operation: GET /dataservice/statistics/system
---------------------------------------------


Get stats raw data

.. code:: python

    def get_stat_data_raw_data_17(
        query: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
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
        client.statistics.system.get_stat_data_raw_data_17()


Operation: POST /dataservice/statistics/system
----------------------------------------------


Get stats raw data

.. code:: python

    def get_stats_raw_data_18(
        payload: Optional[Any] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
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
        client.statistics.system.get_stats_raw_data_18()


.. toctree::
    :maxdepth: 1

    aggregation
    cpu
    csv
    doccount
    fields
    memory
    page
    query/index
    stats/index

