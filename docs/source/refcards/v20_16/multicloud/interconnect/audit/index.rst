=============================
multicloud.interconnect.audit
=============================


Operation: GET /dataservice/multicloud/interconnect/audit
---------------------------------------------------------


API to generate audit report for resources.

.. code:: python

    def get(
        interconnect_type: str,
        connection_type: Optional[str] = None,
        cloud_type: Optional[str] = None,
        device_links: Optional[str] = "false",
        refresh: Optional[str] = "true",
    ) -> AuditReport: ...


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
        client.multicloud.interconnect.audit.get()


.. toctree::
    :maxdepth: 1

    models

