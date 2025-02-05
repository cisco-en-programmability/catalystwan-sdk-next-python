===========
server.info
===========


Operation: GET /dataservice/server/info
---------------------------------------


Get Server info

.. code:: python

    def create_server_info_1() -> Any: ...


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
        client.server.info.create_server_info_1()


