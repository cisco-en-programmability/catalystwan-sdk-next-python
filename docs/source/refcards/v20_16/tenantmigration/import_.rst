=======================
tenantmigration.import_
=======================


Operation: POST /dataservice/tenantmigration/import/{migrationKey}
------------------------------------------------------------------


Import tenant data

.. code:: python

    def post(migration_key: str) -> Any: ...


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
        client.tenantmigration.import_.post()


