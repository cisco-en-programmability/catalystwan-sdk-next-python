=========================
disasterrecovery.schedule
=========================


Operation: GET /dataservice/disasterrecovery/schedule
-----------------------------------------------------


Get disaster recovery local replication schedule

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
        client.disasterrecovery.schedule.get()


