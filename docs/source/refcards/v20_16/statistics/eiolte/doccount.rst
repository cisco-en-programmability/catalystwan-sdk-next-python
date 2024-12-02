==========================
statistics.eiolte.doccount
==========================


Operation: GET /dataservice/statistics/eiolte/doccount
------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_8(query: str) -> Any: ...


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
        client.statistics.eiolte.doccount.get_count_8()


Operation: POST /dataservice/statistics/eiolte/doccount
-------------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post_8(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.eiolte.doccount.get_count_post_8()


