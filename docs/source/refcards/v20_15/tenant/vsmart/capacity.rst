======================
tenant.vsmart.capacity
======================


Operation: GET /dataservice/tenant/vsmart/capacity
--------------------------------------------------


Lists all the vsmarts on the vManage and its tenant hosting capacity<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_tenant_hosting_capacity_onv_smarts() -> List[Any]: ...


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
        client.tenant.vsmart.capacity.get_tenant_hosting_capacity_onv_smarts()


