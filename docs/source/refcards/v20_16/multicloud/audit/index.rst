================
multicloud.audit
================


Operation: GET /dataservice/multicloud/audit
--------------------------------------------


Call an audit with dry run

.. code:: python

    def audit_dry_run(
        cloud_type: CloudTypeParam,
        cloud_region: Optional[str] = None,
        refresh: Optional[str] = "true",
    ) -> None: ...


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
        client.multicloud.audit.audit_dry_run()


Operation: POST /dataservice/multicloud/audit
---------------------------------------------


Call an audit

.. code:: python

    def audit(payload: Optional[AuditFix] = None) -> Taskid: ...


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
        client.multicloud.audit.audit()


.. toctree::
    :maxdepth: 1

    models

