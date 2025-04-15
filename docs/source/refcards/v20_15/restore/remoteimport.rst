====================
restore.remoteimport
====================


Operation: POST /dataservice/restore/remoteimport
-------------------------------------------------


Remote import backup from a remote URL and import the data and apply it to the configuraion database

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.restore.remoteimport.post()


