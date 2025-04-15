=========================
cluster_management.iplist
=========================


Operation: GET /dataservice/clusterManagement/iplist/{vmanageID}
----------------------------------------------------------------


Get configured IP addresses<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get(vmanage_id: str) -> List[Any]: ...


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
        client.cluster_management.iplist.get()


