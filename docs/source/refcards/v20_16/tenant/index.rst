======
tenant
======


Operation: POST /dataservice/tenant
-----------------------------------


Deprecated!!!

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


Operation: PUT /dataservice/tenant
----------------------------------


.. code:: python

    @overload
    def put(payload: Any) -> Any: ...


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


Operation: PUT /dataservice/tenant/{tenantId}
---------------------------------------------


.. code:: python

    @overload
    def put(payload: Any, tenant_id: str) -> Any: ...


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


.. toctree::
    :maxdepth: 1

    async_
    bulk/index
    vsmart/index
    delete
    switch
    vsessionid

