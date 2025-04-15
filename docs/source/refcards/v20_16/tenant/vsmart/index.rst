=============
tenant.vsmart
=============


Operation: GET /dataservice/tenant/vsmart
-----------------------------------------


Retrieve mapping of tenants to vSmarts<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get() -> List[Any]: ...


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
        client.tenant.vsmart.get()


Operation: PUT /dataservice/tenant/{tenantId}/vsmart
----------------------------------------------------


Update placement of the Tenant from source vSmart to destination vSmart<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def put(tenant_id: str, payload: Any) -> List[Any]: ...


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
        client.tenant.vsmart.put()


.. toctree::
    :maxdepth: 1

    capacity

