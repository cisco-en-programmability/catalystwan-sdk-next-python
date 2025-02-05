==================
util.configdb.size
==================


Operation: GET /dataservice/util/configdb/size
----------------------------------------------


Fetches the disk usage by configuration-db

.. code:: python

    def get_db_size_on_file() -> Any: ...


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
        client.util.configdb.size.get_db_size_on_file()


