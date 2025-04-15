==========================================
disasterrecovery.unpause_local_replication
==========================================


Operation: POST /dataservice/disasterrecovery/unpauseLocalReplication
---------------------------------------------------------------------


Unpause DR replication for local datacenter

.. code:: python

    def post() -> Any: ...


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
        client.disasterrecovery.unpause_local_replication.post()


