=============
tenant.async_
=============


Operation: POST /dataservice/tenant/async
-----------------------------------------


Create a new tenant in Multi-Tenant vManage asynchronously<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def create_tenant_async(payload: Optional[Any] = None) -> Any: ...


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
        client.tenant.async_.create_tenant_async()


