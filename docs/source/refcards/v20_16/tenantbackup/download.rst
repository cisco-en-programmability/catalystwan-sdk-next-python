=====================
tenantbackup.download
=====================


Operation: GET /dataservice/tenantbackup/download/{path}
--------------------------------------------------------


Download a Backup File that is already stored in vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def download_existing_backup_file(path: str) -> Any: ...


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
        client.tenantbackup.download.download_existing_backup_file()


