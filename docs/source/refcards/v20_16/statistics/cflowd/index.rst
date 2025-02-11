=================
statistics.cflowd
=================


Operation: GET /dataservice/statistics/cflowd
---------------------------------------------


Get stats raw data

.. code:: python

    def get_stat_data_raw_data_9(
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
        client.statistics.cflowd.get_stat_data_raw_data_9()


Operation: POST /dataservice/statistics/cflowd
----------------------------------------------


Get stats raw data

.. code:: python

    def get_stats_raw_data_9(
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
        client.statistics.cflowd.get_stats_raw_data_9()


.. toctree::
    :maxdepth: 1

    aggregation
    applications/index
    csv
    device/index
    doccount
    fields
    page
    query/index

