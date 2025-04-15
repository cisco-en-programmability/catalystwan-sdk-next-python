===========
backup.list
===========


Operation: GET /dataservice/backup/list
---------------------------------------


List all backup files of a tenant stored in vManage

.. code:: python

    def get(size: Optional[str] = None) -> LocalBackupListResult: ...


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
        client.backup.list.get()


.. toctree::
    :maxdepth: 1

    models

