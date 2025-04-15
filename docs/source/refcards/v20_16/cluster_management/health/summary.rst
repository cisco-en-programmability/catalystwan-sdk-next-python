=================================
cluster_management.health.summary
=================================


Operation: GET /dataservice/clusterManagement/health/summary
------------------------------------------------------------


Get cluster health check summary<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get(
        is_cached: Optional[bool] = False, site_id: Optional[str] = None
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
        client.cluster_management.health.summary.get()


