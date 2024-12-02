==================
util.logging.level
==================


Operation: POST /dataservice/util/logging/level
-----------------------------------------------


Set log level for logger

.. code:: python

    def set_log_level(
        payload: Optional[SetLogLevelPostRequest] = None,
    ) -> None: ...


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
        client.util.logging.level.set_log_level()


.. toctree::
    :maxdepth: 1

    models

