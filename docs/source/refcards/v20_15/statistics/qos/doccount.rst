=======================
statistics.qos.doccount
=======================


Operation: GET /dataservice/statistics/qos/doccount
---------------------------------------------------


Get response count of a query

.. code:: python

    def get_count13(query: str) -> Any: ...


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
        client.statistics.qos.doccount.get_count13()


Operation: POST /dataservice/statistics/qos/doccount
----------------------------------------------------


Get response count of a query

.. code:: python

    def get_count_post13(payload: Optional[Any] = None) -> Any: ...


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
        client.statistics.qos.doccount.get_count_post13()


