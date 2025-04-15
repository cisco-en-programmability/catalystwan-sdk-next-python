===========================
disasterrecovery.deregister
===========================


Operation: POST /dataservice/disasterrecovery/deregister
--------------------------------------------------------


Delete disaster recovery

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
        client.disasterrecovery.deregister.post()


