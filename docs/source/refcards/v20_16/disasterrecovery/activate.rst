=========================
disasterrecovery.activate
=========================


Operation: POST /dataservice/disasterrecovery/activate
------------------------------------------------------


Activate cluster to start working as primary

.. code:: python

    def activate() -> Any: ...


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
        client.disasterrecovery.activate.activate()


