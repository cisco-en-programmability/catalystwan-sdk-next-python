====================
tenantbackup.import_
====================


Operation: POST /dataservice/tenantbackup/import
------------------------------------------------


Submit a previously backed up file and import the data and apply it to the configuraion database<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def import_tenant_backup() -> Any: ...


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
        client.tenantbackup.import_.import_tenant_backup()


