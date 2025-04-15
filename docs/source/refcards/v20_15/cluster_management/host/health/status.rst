=====================================
cluster_management.host.health.status
=====================================


Operation: GET /dataservice/clusterManagement/host/health/status
----------------------------------------------------------------


Get vManage cluster health check details<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

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
        client.cluster_management.host.health.status.get()


