=============================
device.appqoe.cluster_summary
=============================


Operation: GET /dataservice/device/appqoe/cluster-summary
---------------------------------------------------------


Get Appqoe Cluster Summary from device

.. code:: python

    def get_appqoe_cluster_summary(device_id: str) -> Any: ...


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
        client.device.appqoe.cluster_summary.get_appqoe_cluster_summary()


