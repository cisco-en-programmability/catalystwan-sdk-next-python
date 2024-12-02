=================
backup.backupinfo
=================


Operation: DELETE /dataservice/backup/backupinfo
------------------------------------------------


Delete all or a specific backup file stored in vManage

.. code:: python

    def delete_schduled_backup(
        task_id: Optional[str] = None,
        backup_info_id: Optional[str] = None,
    ) -> Any: ...


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
        client.backup.backupinfo.delete_schduled_backup()


Operation: GET /dataservice/backup/backupinfo/{localBackupInfoId}
-----------------------------------------------------------------


Get a localBackupInfo record by localBackupInfoId

.. code:: python

    def get_local_backup_info(
        local_backup_info_id: str,
    ) -> LocalBackupInfo: ...


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
        client.backup.backupinfo.get_local_backup_info()


.. toctree::
    :maxdepth: 1

    models

