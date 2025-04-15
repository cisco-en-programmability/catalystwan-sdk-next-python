========================
cluster_management.setup
========================


Operation: PUT /dataservice/clusterManagement/setup
---------------------------------------------------


Update vManage cluster info<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def put(payload: Any) -> None: ...


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
        client.cluster_management.setup.put()


Operation: POST /dataservice/clusterManagement/setup
----------------------------------------------------


Add vManage to cluster

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
        client.cluster_management.setup.post()


