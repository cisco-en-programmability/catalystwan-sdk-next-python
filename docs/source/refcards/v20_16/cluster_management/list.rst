=======================
cluster_management.list
=======================


Operation: GET /dataservice/clusterManagement/list
--------------------------------------------------


List vManages in the cluster<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def list_vmanages() -> List[Any]: ...


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
        client.cluster_management.list.list_vmanages()


