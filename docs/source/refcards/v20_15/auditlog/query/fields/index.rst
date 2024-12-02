=====================
auditlog.query.fields
=====================


Operation: GET /dataservice/auditlog/query/fields
-------------------------------------------------


Get query fields

.. code:: python

    def get_stat_query_fields() -> List[GetStatQueryFields]: ...


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
        client.auditlog.query.fields.get_stat_query_fields()


.. toctree::
    :maxdepth: 1

    models

