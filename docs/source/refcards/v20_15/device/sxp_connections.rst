======================
device.sxp_connections
======================


Operation: GET /dataservice/device/sxpConnections
-------------------------------------------------


get Cisco TrustSec SXP Connections information from device

.. code:: python

    def get_sxp_connections(device_id: str) -> Any: ...


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
        client.device.sxp_connections.get_sxp_connections()


