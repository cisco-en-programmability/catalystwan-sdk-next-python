==============================
statistics.cflowd.query.fields
==============================


Operation: GET /dataservice/statistics/cflowd/query/fields
----------------------------------------------------------


Get query fields

.. code:: python

    def get_stat_query_fields_10() -> Any: ...


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
        client.statistics.cflowd.query.fields.get_stat_query_fields_10()


