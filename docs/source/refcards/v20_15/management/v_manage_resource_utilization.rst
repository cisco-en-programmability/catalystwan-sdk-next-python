========================================
management.v_manage_resource_utilization
========================================


Operation: GET /dataservice/management/vManageResourceUtilization
-----------------------------------------------------------------


Get vManage resource utilization

.. code:: python

    def get() -> Any: ...


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
        client.management.v_manage_resource_utilization.get()


