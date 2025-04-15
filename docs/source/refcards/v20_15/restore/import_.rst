===============
restore.import_
===============


Operation: POST /dataservice/restore/import
-------------------------------------------


Submit a previously backed up file and import the data and apply it to the configuraion database

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
        client.restore.import_.post()


