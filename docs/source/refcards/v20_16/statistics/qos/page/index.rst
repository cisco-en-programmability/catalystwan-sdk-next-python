===================
statistics.qos.page
===================


Operation: GET /dataservice/statistics/qos/page
-----------------------------------------------


Get stats raw data

.. code:: python

    def get_stat_bulk_raw_data_2(
        query: Optional[str] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
    ) -> QoSRespWithPageInfo: ...


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
        client.statistics.qos.page.get_stat_bulk_raw_data_2()


Operation: POST /dataservice/statistics/qos/page
------------------------------------------------


Get stats raw data

.. code:: python

    def get_post_stat_bulk_raw_data12(
        payload: Optional[Any] = None,
        scroll_id: Optional[str] = None,
        count: Optional[int] = None,
    ) -> QoSRespWithPageInfo: ...


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
        client.statistics.qos.page.get_post_stat_bulk_raw_data12()


.. toctree::
    :maxdepth: 1

    models

