=================
auditlog.severity
=================


Operation: GET /dataservice/auditlog/severity
---------------------------------------------


Get audit logs for last 3 hours

.. code:: python

    def generate_audit_log(
        query: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[SortOrderParam] = None,
        site_id: Optional[str] = None,
    ) -> GetAuditLogBySeverity: ...


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
        client.auditlog.severity.generate_audit_log()


.. toctree::
    :maxdepth: 1

    summary/index
    models

