======================
disasterrecovery.pause
======================


Operation: POST /dataservice/disasterrecovery/pause
---------------------------------------------------


Pause DR

.. code:: python

    def pause_dr() -> Any: ...


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
        client.disasterrecovery.pause.pause_dr()


