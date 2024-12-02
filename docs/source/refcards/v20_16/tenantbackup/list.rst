=================
tenantbackup.list
=================


Operation: GET /dataservice/tenantbackup/list
---------------------------------------------


List all backup files of a tenant stored in vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def list_tenant_backup() -> Any: ...


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
        client.tenantbackup.list.list_tenant_backup()


