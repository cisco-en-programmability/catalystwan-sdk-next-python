=============
tenant.vsmart
=============


Operation: GET /dataservice/tenant/vsmart
-----------------------------------------


Retrieve mapping of tenants to vSmarts<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_tenantv_smart_mapping() -> List[Any]: ...


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
        client.tenant.vsmart.get_tenantv_smart_mapping()


Operation: PUT /dataservice/tenant/{tenantId}/vsmart
----------------------------------------------------


Update placement of the Tenant from source vSmart to destination vSmart<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def update_tenantv_smart_placement(
        tenant_id: str, payload: Optional[Any] = None
    ) -> List[Any]: ...


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
        client.tenant.vsmart.update_tenantv_smart_placement()


.. toctree::
    :maxdepth: 1

    capacity

