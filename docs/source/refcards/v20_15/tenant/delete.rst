=============
tenant.delete
=============


Operation: POST /dataservice/tenant/{tenantId}/delete
-----------------------------------------------------


Delete a tenant by Id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def delete_tenant(
        tenant_id: str, payload: Optional[Any] = None
    ) -> None: ...


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
        client.tenant.delete.delete_tenant()


