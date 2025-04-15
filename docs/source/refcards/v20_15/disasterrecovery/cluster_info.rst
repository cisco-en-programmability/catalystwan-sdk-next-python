=============================
disasterrecovery.cluster_info
=============================


Operation: GET /dataservice/disasterrecovery/clusterInfo
--------------------------------------------------------


Get disaster recovery cluster info

.. code:: python

    def get() -> Any: ...


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
        client.disasterrecovery.cluster_info.get()


