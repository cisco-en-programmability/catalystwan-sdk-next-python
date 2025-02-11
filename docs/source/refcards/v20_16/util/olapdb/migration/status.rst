============================
util.olapdb.migration.status
============================


Operation: GET /dataservice/util/olapdb/migration/status
--------------------------------------------------------


Deprecated!!!

Get migration status

.. code:: python

    def get_stats_migration_status() -> Any: ...


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
        client.util.olapdb.migration.status.get_stats_migration_status()


