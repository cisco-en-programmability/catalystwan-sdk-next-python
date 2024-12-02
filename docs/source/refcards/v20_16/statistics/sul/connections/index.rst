==========================
statistics.sul.connections
==========================


Operation: GET /dataservice/statistics/sul/connections
------------------------------------------------------


Get security connection events stats raw data

.. code:: python

    def get_sul_stat_data_raw_data(
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
        client.statistics.sul.connections.get_sul_stat_data_raw_data()


Operation: POST /dataservice/statistics/sul/connections
-------------------------------------------------------


Get stats raw data

.. code:: python

    def get_stats_raw_data_16(
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
        client.statistics.sul.connections.get_stats_raw_data_16()


.. toctree::
    :maxdepth: 1

    aggregation
    app_agg/index
    csv
    doccount
    fields
    filter/index
    page
    query/index

