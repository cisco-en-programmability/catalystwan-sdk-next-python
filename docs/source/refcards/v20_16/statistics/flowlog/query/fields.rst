===============================
statistics.flowlog.query.fields
===============================


Operation: GET /dataservice/statistics/flowlog/query/fields
-----------------------------------------------------------


Get query fields

.. code:: python

    def get_flowlog_query_fields() -> Any: ...


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
        client.statistics.flowlog.query.fields.get_flowlog_query_fields()


