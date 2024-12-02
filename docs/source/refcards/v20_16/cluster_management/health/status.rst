================================
cluster_management.health.status
================================


Operation: GET /dataservice/clusterManagement/health/status
-----------------------------------------------------------


Get cluster health check details<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def health_status_info() -> Any: ...


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
        client.cluster_management.health.status.health_status_info()


