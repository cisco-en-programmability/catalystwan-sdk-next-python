==========================
cluster_management.isready
==========================


Operation: GET /dataservice/clusterManagement/isready
-----------------------------------------------------


Is cluster ready<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def is_cluster_ready() -> Any: ...


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
        client.cluster_management.isready.is_cluster_ready()


