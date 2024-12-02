================================
disasterrecovery.dbrestorestatus
================================


Operation: GET /dataservice/disasterrecovery/dbrestorestatus
------------------------------------------------------------


Config-db restore status

.. code:: python

    def get_config_db_restore_status() -> List[Any]: ...


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
        client.disasterrecovery.dbrestorestatus.get_config_db_restore_status()


