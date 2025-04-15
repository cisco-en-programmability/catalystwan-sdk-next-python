=================
auditlog.doccount
=================


Operation: GET /dataservice/auditlog/doccount
---------------------------------------------


Get response count of a query

.. code:: python

    def get(query: str) -> GetAuditLogDoccount: ...


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
        client.auditlog.doccount.get()


Operation: POST /dataservice/auditlog/doccount
----------------------------------------------


Get response count of a query

.. code:: python

    def post(payload: Any) -> GetAuditLogDoccount: ...


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
        client.auditlog.doccount.post()


.. toctree::
    :maxdepth: 1

    models

