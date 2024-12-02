==================================
statistics.wlanclientinfo.doccount
==================================


Operation: GET /dataservice/statistics/wlanclientinfo/doccount
--------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_19(query: str) -> Any: ...


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
        client.statistics.wlanclientinfo.doccount.get_count_19()


Operation: POST /dataservice/statistics/wlanclientinfo/doccount
---------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_19(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.wlanclientinfo.doccount.get_count_post_19()


