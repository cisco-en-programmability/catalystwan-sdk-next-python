=========================
auditlog.severity.summary
=========================


Operation: GET /dataservice/auditlog/severity/summary
-----------------------------------------------------


Get audit log severity histogram

.. code:: python

    def get_audit_severity_custom_histogram(
        query: str,
    ) -> InlineResponse200: ...


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
        client.auditlog.severity.summary.get_audit_severity_custom_histogram()


.. toctree::
    :maxdepth: 1

    models

