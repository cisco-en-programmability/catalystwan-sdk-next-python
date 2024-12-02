=============
tenant.switch
=============


Operation: POST /dataservice/tenant/{tenantId}/switch
-----------------------------------------------------


Switch to a specific tenant<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def switch_tenant(tenant_id: str) -> Any: ...


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
        client.tenant.switch.switch_tenant()


