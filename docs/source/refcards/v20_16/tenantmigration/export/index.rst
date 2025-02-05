======================
tenantmigration.export
======================


Operation: POST /dataservice/tenantmigration/export
---------------------------------------------------


Export tenant data

.. code:: python

    def export_tenant_data(
        payload: Optional[MigrateTenantModel] = None,
    ) -> Any: ...


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
        client.tenantmigration.export.export_tenant_data()


.. toctree::
    :maxdepth: 1

    models

