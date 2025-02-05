=================================
util.olapdb.migration.statsdbinfo
=================================


Operation: GET /dataservice/util/olapdb/migration/statsdbinfo
-------------------------------------------------------------


Deprecated!!!

Get stats db table information

.. code:: python

    def get_stats_migration_stats_db_info() -> Any: ...


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
        client.util.olapdb.migration.statsdbinfo.get_stats_migration_stats_db_info()


