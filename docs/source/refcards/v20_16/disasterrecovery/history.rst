========================
disasterrecovery.history
========================


Operation: GET /dataservice/disasterrecovery/history
----------------------------------------------------


Get disaster recovery switchover history

.. code:: python

    def get_history() -> Any: ...


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
        client.disasterrecovery.history.get_history()


