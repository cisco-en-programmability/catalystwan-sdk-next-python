=====================================
device.environment_data.radius_server
=====================================


Operation: GET /dataservice/device/environmentData/radiusServer
---------------------------------------------------------------


get Cisco TrustSec Environment Data Radius Server list from device

.. code:: python

    def get_radius_server(device_id: str) -> Any: ...


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
        client.device.environment_data.radius_server.get_radius_server()


