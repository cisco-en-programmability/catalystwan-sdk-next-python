=============================
statistics.interface.doccount
=============================


Operation: GET /dataservice/statistics/interface/doccount
---------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count10(query: str) -> Any: ...


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
        client.statistics.interface.doccount.get_count10()


Operation: POST /dataservice/statistics/interface/doccount
----------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_11(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.interface.doccount.get_count_post_11()


