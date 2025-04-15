==========================================
cluster_management.replicate_and_rebalance
==========================================


Operation: PUT /dataservice/clusterManagement/replicateAndRebalance
-------------------------------------------------------------------


Initiate replication and rebalance of kafka topics<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def put() -> Any: ...


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
        client.cluster_management.replicate_and_rebalance.put()


