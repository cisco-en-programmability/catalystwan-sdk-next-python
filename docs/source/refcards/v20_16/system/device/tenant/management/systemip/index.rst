========================================
system.device.tenant.management.systemip
========================================


Operation: GET /dataservice/system/device/tenant/management/systemip
--------------------------------------------------------------------


Get management system IP<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_tenant_management_system_i_ps() -> (
        List[GetTenantManagementSystemIPsInner]
    ): ...


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
        client.system.device.tenant.management.systemip.get_tenant_management_system_i_ps()


.. toctree::
    :maxdepth: 1

    models

