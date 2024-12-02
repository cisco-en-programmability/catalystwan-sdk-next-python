=================================
cluster_management.cluster_locked
=================================


Operation: GET /dataservice/clusterManagement/clusterLocked
-----------------------------------------------------------


Check whether cluster is locked<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def check_if_cluster_locked() -> Any: ...


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
        client.cluster_management.cluster_locked.check_if_cluster_locked()


