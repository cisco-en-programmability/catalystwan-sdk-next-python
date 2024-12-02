==============
device.history
==============


Operation: GET /dataservice/device/history
------------------------------------------


Get stats raw data

.. code:: python

    def get_stat_data_raw_data_21(
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
        client.device.history.get_stat_data_raw_data_21()


Operation: POST /dataservice/device/history
-------------------------------------------


Get stats raw data

.. code:: python

    def get_stats_raw_data_22(
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
        client.device.history.get_stats_raw_data_22()


.. toctree::
    :maxdepth: 1

    aggregation
    config/index
    csv
    doccount
    fields
    page
    query/index

