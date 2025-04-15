========
auditlog
========


Operation: GET /dataservice/auditlog
------------------------------------


Get stat raw data

.. code:: python

    def get(query: str) -> GetAuditLogData: ...


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
        client.auditlog.get()


Operation: POST /dataservice/auditlog
-------------------------------------


Get raw property data with post action

.. code:: python

    def post(payload: Any) -> GetAuditLogData: ...


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
        client.auditlog.post()


.. toctree::
    :maxdepth: 1

    aggregation/index
    doccount/index
    fields/index
    page/index
    query/index
    severity/index
    models

