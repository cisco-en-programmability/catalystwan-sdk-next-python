============================
util.olapdb.migration.action
============================


Operation: POST /dataservice/util/olapdb/migration/action/{action}
------------------------------------------------------------------


Migration actions - start pause or restart migration

.. code:: python

    def post(action: ActionParam) -> str: ...


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
        client.util.olapdb.migration.action.post()


.. toctree::
    :maxdepth: 1

    models

