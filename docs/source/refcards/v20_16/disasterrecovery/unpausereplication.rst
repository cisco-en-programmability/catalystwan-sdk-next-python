===================================
disasterrecovery.unpausereplication
===================================


Operation: POST /dataservice/disasterrecovery/unpausereplication
----------------------------------------------------------------


Deprecated!!!

Un-Pause DR data replication

.. code:: python

    def disaster_recovery_un_pause_replication() -> Any: ...


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
        client.disasterrecovery.unpausereplication.disaster_recovery_un_pause_replication()


