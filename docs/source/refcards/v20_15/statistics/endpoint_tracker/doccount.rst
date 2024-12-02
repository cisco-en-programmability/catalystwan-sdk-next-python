====================================
statistics.endpoint_tracker.doccount
====================================


Operation: GET /dataservice/statistics/endpointTracker/doccount
---------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_18(query: str) -> Any: ...


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
        client.statistics.endpoint_tracker.doccount.get_count_18()


Operation: POST /dataservice/statistics/endpointTracker/doccount
----------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_18(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.endpoint_tracker.doccount.get_count_post_18()


