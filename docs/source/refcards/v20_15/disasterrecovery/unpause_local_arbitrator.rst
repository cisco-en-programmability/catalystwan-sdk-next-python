=========================================
disasterrecovery.unpause_local_arbitrator
=========================================


Operation: POST /dataservice/disasterrecovery/unpauseLocalArbitrator
--------------------------------------------------------------------


Unpause DR for Local Arbitrator

.. code:: python

    def unpause_local_arbitrator() -> Any: ...


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
        client.disasterrecovery.unpause_local_arbitrator.unpause_local_arbitrator()


