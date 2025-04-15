==========
ump.status
==========


Operation: GET /dataservice/ump/status
--------------------------------------


Get last N minutes UMP historic data

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
        client.ump.status.get()


