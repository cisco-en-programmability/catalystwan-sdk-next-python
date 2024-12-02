======
tenant
======


Operation: GET /dataservice/tenant
----------------------------------


Lists all the tenants on the vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_all_tenants(device_id: Optional[str] = None) -> List[Any]: ...


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
        client.tenant.get_all_tenants()


Operation: POST /dataservice/tenant
-----------------------------------


Create a new tenant in Multi-Tenant vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def create_tenant(payload: Optional[Any] = None) -> Any: ...


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
        client.tenant.create_tenant()


Operation: GET /dataservice/tenant/{tenantId}
---------------------------------------------


Get a tenant by Id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_tenant(tenant_id: str) -> Any: ...


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
        client.tenant.get_tenant()


Operation: PUT /dataservice/tenant/{tenantId}
---------------------------------------------


Update a tenant in Multi-Tenant vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def update_tenant(
        tenant_id: str, payload: Optional[Any] = None
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
        client.tenant.update_tenant()


.. toctree::
    :maxdepth: 1

    async_
    bulk/index
    vsmart/index
    vsmart_mt/index
    delete
    switch
    vsessionid

