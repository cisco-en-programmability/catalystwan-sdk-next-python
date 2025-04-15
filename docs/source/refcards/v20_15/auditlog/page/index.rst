=============
auditlog.page
=============


Operation: GET /dataservice/auditlog/page
-----------------------------------------


Get raw property data in bulk

.. code:: python

    def get(
        query: str, count: int, scroll_id: Optional[str] = None
    ) -> GetAuditLogData: ...


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
        client.auditlog.page.get()


Operation: POST /dataservice/auditlog/page
------------------------------------------


Get raw property data in bulk with post action

.. code:: python

    def post(
        count: int, payload: Any, scroll_id: Optional[str] = None
    ) -> GetAuditLogData: ...


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
        client.auditlog.page.post()


.. toctree::
    :maxdepth: 1

    models

