===================================
cluster_management.v_manage.details
===================================


Operation: GET /dataservice/clusterManagement/vManage/details/{vmanageIP}
-------------------------------------------------------------------------


Get vManage detail<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_v_manage_details(vmanage_ip: str) -> Any: ...


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
        client.cluster_management.v_manage.details.get_v_manage_details()


