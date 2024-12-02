=========================
statistics.interface.page
=========================


Operation: GET /dataservice/statistics/interface/page
-----------------------------------------------------


Get stats raw data

.. code:: python

    def get_stat_bulk_raw_data_2(
        query: str, count: str, scroll_id: Optional[str] = None
    ) -> InterfaceAggRespWithPageInfo: ...


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
        client.statistics.interface.page.get_stat_bulk_raw_data_2()


Operation: POST /dataservice/statistics/interface/page
------------------------------------------------------


Get stats raw data

.. code:: python

    def get_post_stat_bulk_raw_data_2(
        count: str,
        payload: Optional[Any] = None,
        scroll_id: Optional[str] = None,
    ) -> InterfaceAggRespWithPageInfo: ...


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
        client.statistics.interface.page.get_post_stat_bulk_raw_data_2()


.. toctree::
    :maxdepth: 1

    models

