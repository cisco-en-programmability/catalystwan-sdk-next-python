==================
tenant.bulk.async_
==================


Operation: POST /dataservice/tenant/bulk/async
----------------------------------------------


Create multiple tenants on vManage asynchronously<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def create_tenant_async_bulk(
        payload: Optional[Any] = None,
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
        client.tenant.bulk.async_.create_tenant_async_bulk()


Operation: DELETE /dataservice/tenant/bulk/async
------------------------------------------------


Delete multiple tenants on vManage asynchronously<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def delete_tenant_async_bulk(
        payload: Optional[Any] = None,
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
        client.tenant.bulk.async_.delete_tenant_async_bulk()


