==============================
cluster_management.tenant_list
==============================


Operation: GET /dataservice/clusterManagement/tenantList
--------------------------------------------------------


Get tenant list<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

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
        client.cluster_management.tenant_list.get()


