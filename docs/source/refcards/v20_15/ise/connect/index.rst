===========
ise.connect
===========


Operation: GET /dataservice/ise/connect
---------------------------------------


Check if the configured ISE server is reachable

.. code:: python

    def get() -> ConnectResponse: ...


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
        client.ise.connect.get()


.. toctree::
    :maxdepth: 1

    models

