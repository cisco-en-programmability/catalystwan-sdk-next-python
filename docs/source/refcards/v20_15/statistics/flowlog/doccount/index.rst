===========================
statistics.flowlog.doccount
===========================


Operation: GET /dataservice/statistics/flowlog/doccount
-------------------------------------------------------


Get response count of a query

.. code:: python

    def get(query: str) -> CountResponse: ...


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
        client.statistics.flowlog.doccount.get()


Operation: POST /dataservice/statistics/flowlog/doccount
--------------------------------------------------------


Get response count of a query

.. code:: python

    def post(payload: Any) -> CountResponse: ...


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
        client.statistics.flowlog.doccount.post()


.. toctree::
    :maxdepth: 1

    models

