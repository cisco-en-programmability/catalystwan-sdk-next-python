=======================
multicloud.devices.edge
=======================


Operation: GET /dataservice/multicloud/devices/edge/{edgeType}
--------------------------------------------------------------


Deprecated!!!

Get cloud devices by cloud type

.. code:: python

    def get_cloud_devices_1(
        edge_type: str, edge_gateway_name: Optional[str] = None
    ) -> Any: ...


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
        client.multicloud.devices.edge.get_cloud_devices_1()


