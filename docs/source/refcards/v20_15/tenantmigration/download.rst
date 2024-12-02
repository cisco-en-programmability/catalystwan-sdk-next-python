========================
tenantmigration.download
========================


Operation: GET /dataservice/tenantmigration/download/{path}
-----------------------------------------------------------


Download tenant data

.. code:: python

    def download_tenant_data(path: str) -> Any: ...


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
        client.tenantmigration.download.download_tenant_data()


