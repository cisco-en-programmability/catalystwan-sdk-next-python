==============================
statistics.apphostinginterface
==============================


Operation: GET /dataservice/statistics/apphostinginterface
----------------------------------------------------------


Get stats raw data

.. code:: python

    def get_stat_data_raw_data(
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
        client.statistics.apphostinginterface.get_stat_data_raw_data()


Operation: POST /dataservice/statistics/apphostinginterface
-----------------------------------------------------------


Get stats raw data

.. code:: python

    def get_stats_raw_data(
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
        client.statistics.apphostinginterface.get_stats_raw_data()


.. toctree::
    :maxdepth: 1

    aggregation
    csv
    doccount
    fields
    page
    query/index

