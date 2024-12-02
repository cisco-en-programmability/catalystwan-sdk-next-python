===========================================
statistics.apphostinginterface.query.fields
===========================================


Operation: GET /dataservice/statistics/apphostinginterface/query/fields
-----------------------------------------------------------------------


Get query fields

.. code:: python

    def get_stat_query_fields_1() -> Any: ...


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
        client.statistics.apphostinginterface.query.fields.get_stat_query_fields_1()


