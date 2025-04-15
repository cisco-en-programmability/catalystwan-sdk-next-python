==========================
statistics.system.doccount
==========================


Operation: GET /dataservice/statistics/system/doccount
------------------------------------------------------


Get response count of a query

.. code:: python

    def get(query: str) -> Any: ...


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
        client.statistics.system.doccount.get()


Operation: POST /dataservice/statistics/system/doccount
-------------------------------------------------------


Get response count of a query

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.statistics.system.doccount.post()


