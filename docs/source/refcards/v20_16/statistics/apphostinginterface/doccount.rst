=======================================
statistics.apphostinginterface.doccount
=======================================


Operation: GET /dataservice/statistics/apphostinginterface/doccount
-------------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_1(query: str) -> Any: ...


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
        client.statistics.apphostinginterface.doccount.get_count_1()


Operation: POST /dataservice/statistics/apphostinginterface/doccount
--------------------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_1(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.apphostinginterface.doccount.get_count_post_1()


