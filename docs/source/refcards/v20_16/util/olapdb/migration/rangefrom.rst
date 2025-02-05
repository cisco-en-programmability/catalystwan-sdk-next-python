===============================
util.olapdb.migration.rangefrom
===============================


Operation: GET /dataservice/util/olapdb/migration/rangefrom
-----------------------------------------------------------


Deprecated!!!

Get migration historical data range configuration from upgrade time

.. code:: python

    def get_stats_migration_range_config() -> Any: ...


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
        client.util.olapdb.migration.rangefrom.get_stats_migration_range_config()


Operation: POST /dataservice/util/olapdb/migration/rangefrom
------------------------------------------------------------


Deprecated!!!

Config migration historical data range from upgrade time in seconds. -1 to keep all.

.. code:: python

    def post_stats_migration_range_config(
        payload: Optional[str] = None,
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
        client.util.olapdb.migration.rangefrom.post_stats_migration_range_config()


