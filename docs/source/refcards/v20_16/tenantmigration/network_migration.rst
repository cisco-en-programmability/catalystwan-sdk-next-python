=================================
tenantmigration.network_migration
=================================


Operation: GET /dataservice/tenantmigration/networkMigration
------------------------------------------------------------


Re-trigger network migration

.. code:: python

    def re_trigger_network_migration() -> Any: ...


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
        client.tenantmigration.network_migration.re_trigger_network_migration()


Operation: POST /dataservice/tenantmigration/networkMigration
-------------------------------------------------------------


Migrate network

.. code:: python

    def migrate_network(payload: Optional[Any] = None) -> Any: ...


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
        client.tenantmigration.network_migration.migrate_network()


