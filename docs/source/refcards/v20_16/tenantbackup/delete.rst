===================
tenantbackup.delete
===================


Operation: DELETE /dataservice/tenantbackup/delete
--------------------------------------------------


Delete all or a specific backup file stored in vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def delete_tenant_backup(file_name: str) -> Any: ...


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
        client.tenantbackup.delete.delete_tenant_backup()


