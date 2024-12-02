=================
tenant.vsessionid
=================


Operation: POST /dataservice/tenant/{tenantId}/vsessionid
---------------------------------------------------------


Get VSessionId for a specific tenant<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def v_session_id(tenant_id: str) -> Any: ...


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
        client.tenant.vsessionid.v_session_id()


