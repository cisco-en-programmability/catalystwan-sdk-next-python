=================================
tenantmigration.network_migration
=================================


Operation: GET /dataservice/tenantmigration/networkMigration
------------------------------------------------------------


Re-trigger network migration

.. code:: python

    def get() -> Any: ...


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
        client.tenantmigration.network_migration.get()


Operation: POST /dataservice/tenantmigration/networkMigration
-------------------------------------------------------------


Migrate network

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.tenantmigration.network_migration.post()


