==========================
statistics.system.doccount
==========================


Operation: GET /dataservice/statistics/system/doccount
------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_16(query: str) -> Any: ...


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
        client.statistics.system.doccount.get_count_16()


Operation: POST /dataservice/statistics/system/doccount
-------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_17(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.system.doccount.get_count_post_17()


