==============================
util.olapdb.migration.settings
==============================


Operation: GET /dataservice/util/olapdb/migration/settings
----------------------------------------------------------


Get migration generic settings

.. code:: python

    def get_stats_migration_settings() -> Any: ...


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
        client.util.olapdb.migration.settings.get_stats_migration_settings()


Operation: POST /dataservice/util/olapdb/migration/settings
-----------------------------------------------------------


Config generic settings

.. code:: python

    def post_stats_migration_settings(
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
        client.util.olapdb.migration.settings.post_stats_migration_settings()


