======
tenant
======


Operation: POST /dataservice/tenant
-----------------------------------


Create a new tenant in Multi-Tenant vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.tenant.post()


Operation: PUT /dataservice/tenant/{tenantId}
---------------------------------------------


Update a tenant in Multi-Tenant vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def put(tenant_id: str, payload: Any) -> Any: ...


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
        client.tenant.put()


Operation: GET /dataservice/tenant
----------------------------------


.. code:: python

    @overload
    def get(device_id: Optional[str] = None) -> List[Any]: ...


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
        client.tenant.get()


Operation: GET /dataservice/tenant/{tenantId}
---------------------------------------------


.. code:: python

    @overload
    def get(tenant_id: str) -> Any: ...


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
        client.tenant.get()


.. toctree::
    :maxdepth: 1

    async_
    bulk/index
    vsmart/index
    vsmart_mt/index
    delete
    switch
    vsessionid

