============================
cluster_management.configure
============================


Operation: POST /dataservice/clusterManagement/configure
--------------------------------------------------------


Configure vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def configure_vmanage(payload: Optional[Any] = None) -> None: ...


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
        client.cluster_management.configure.configure_vmanage()


