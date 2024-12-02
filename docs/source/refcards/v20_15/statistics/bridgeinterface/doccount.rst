===================================
statistics.bridgeinterface.doccount
===================================


Operation: GET /dataservice/statistics/bridgeinterface/doccount
---------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_7(query: str) -> Any: ...


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
        client.statistics.bridgeinterface.doccount.get_count_7()


Operation: POST /dataservice/statistics/bridgeinterface/doccount
----------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_6(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.bridgeinterface.doccount.get_count_post_6()


