=====================================
disasterrecovery.local_latest_history
=====================================


Operation: GET /dataservice/disasterrecovery/localLatestHistory
---------------------------------------------------------------


Get disaster recovery local switchover history

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
        client.disasterrecovery.local_latest_history.get()


