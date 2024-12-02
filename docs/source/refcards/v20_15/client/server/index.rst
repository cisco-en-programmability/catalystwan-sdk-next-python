=============
client.server
=============


Operation: GET /dataservice/client/server
-----------------------------------------


Get vManage server information

.. code:: python

    def create_server_info() -> ClientServerInfoResponse: ...


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
        client.client.server.create_server_info()


.. toctree::
    :maxdepth: 1

    models

