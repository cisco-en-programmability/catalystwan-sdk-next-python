===============================
tenantmigration.migration_token
===============================


Operation: GET /dataservice/tenantmigration/migrationToken
----------------------------------------------------------


Get migration token

.. code:: python

    def get_migration_token(migration_id: str) -> Any: ...


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
        client.tenantmigration.migration_token.get_migration_token()


