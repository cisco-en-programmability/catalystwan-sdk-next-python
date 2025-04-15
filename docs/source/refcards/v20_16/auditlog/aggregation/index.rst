====================
auditlog.aggregation
====================


Operation: GET /dataservice/auditlog/aggregation
------------------------------------------------


Get raw property data aggregated

.. code:: python

    def get(query: str) -> GetAuditLogAggregation: ...


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
        client.auditlog.aggregation.get()


Operation: POST /dataservice/auditlog/aggregation
-------------------------------------------------


Get raw property data aggregated with post action

.. code:: python

    def post(payload: Any) -> GetAuditLogAggregation: ...


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
        client.auditlog.aggregation.post()


.. toctree::
    :maxdepth: 1

    models

