====================
util.logging.loggers
====================


Operation: GET /dataservice/util/logging/loggers
------------------------------------------------


List loggers

.. code:: python

    def get() -> List[Loggers]: ...


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
        client.util.logging.loggers.get()


.. toctree::
    :maxdepth: 1

    models

