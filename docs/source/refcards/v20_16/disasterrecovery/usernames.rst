==========================
disasterrecovery.usernames
==========================


Operation: GET /dataservice/disasterrecovery/usernames
------------------------------------------------------


Fetch data centers and vBonds usernames for disaster recovery

.. code:: python

    def get(payload: Optional[Any] = None) -> Any: ...


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
        client.disasterrecovery.usernames.get()


