=============================
cluster_management.user_creds
=============================


Operation: POST /dataservice/clusterManagement/userCreds
--------------------------------------------------------


Add or update user credentials for cluster operations<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.cluster_management.user_creds.post()


