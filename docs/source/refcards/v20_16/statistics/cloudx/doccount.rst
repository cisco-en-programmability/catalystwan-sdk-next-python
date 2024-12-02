==========================
statistics.cloudx.doccount
==========================


Operation: GET /dataservice/statistics/cloudx/doccount
------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_10(query: str) -> Any: ...


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
        client.statistics.cloudx.doccount.get_count_10()


Operation: POST /dataservice/statistics/cloudx/doccount
-------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_10(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.cloudx.doccount.get_count_post_10()


