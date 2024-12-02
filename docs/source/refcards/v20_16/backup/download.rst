===============
backup.download
===============


Operation: GET /dataservice/backup/download/{path}
--------------------------------------------------


Download a Backup File that is already stored in vManage

.. code:: python

    def download_backup_file(path: str) -> str: ...


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
        client.backup.download.download_backup_file()


