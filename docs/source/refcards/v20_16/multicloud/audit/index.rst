================
multicloud.audit
================


Operation: GET /dataservice/multicloud/audit
--------------------------------------------


Call an audit with dry run

.. code:: python

    def get(
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
        client.multicloud.audit.get()


Operation: POST /dataservice/multicloud/audit
---------------------------------------------


Call an audit

.. code:: python

    def post(payload: AuditFix) -> Taskid: ...


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
        client.multicloud.audit.post()


.. toctree::
    :maxdepth: 1

    models

