================
umbrella.syncnow
================


Operation: GET /dataservice/umbrella/syncnow
--------------------------------------------


Get metadata from db and send to Umbrella

.. code:: python

    def get() -> None: ...


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
        client.umbrella.syncnow.get()


