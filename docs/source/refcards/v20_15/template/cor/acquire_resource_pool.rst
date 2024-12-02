==================================
template.cor.acquire_resource_pool
==================================


Operation: POST /dataservice/template/cor/acquireResourcePool
-------------------------------------------------------------


Deprecated!!!

Acquire IP from resource pool

.. code:: python

    def acquire_resource_pool(payload: Optional[Any] = None) -> None: ...


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
        client.template.cor.acquire_resource_pool.acquire_resource_pool()


