========================
tenant.vsmart_mt.migrate
========================


Operation: POST /dataservice/tenant/vsmart-mt/migrate
-----------------------------------------------------


Migrate tenants from single tenant vSmarts to multi-tenant capable vSmarts<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def post() -> List[Any]: ...


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
        client.tenant.vsmart_mt.migrate.post()


