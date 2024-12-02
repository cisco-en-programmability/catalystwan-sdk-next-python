==========================================
cluster_management.clusterworkflow.version
==========================================


Operation: GET /dataservice/clusterManagement/clusterworkflow/version
---------------------------------------------------------------------


List vManages in the cluster<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_cluster_workflow_version() -> List[Any]: ...


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
        client.cluster_management.clusterworkflow.version.get_cluster_workflow_version()


