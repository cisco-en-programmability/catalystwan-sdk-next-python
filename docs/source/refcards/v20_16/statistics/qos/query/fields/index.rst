===========================
statistics.qos.query.fields
===========================


Operation: GET /dataservice/statistics/qos/query/fields
-------------------------------------------------------


Get query fields

.. code:: python

    def get_stat_query_fields_14() -> QoSQueryFieldsResp: ...


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
        client.statistics.qos.query.fields.get_stat_query_fields_14()


.. toctree::
    :maxdepth: 1

    models

