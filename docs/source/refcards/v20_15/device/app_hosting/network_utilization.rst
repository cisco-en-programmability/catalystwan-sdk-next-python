======================================
device.app_hosting.network_utilization
======================================


Operation: GET /dataservice/device/app-hosting/network-utilization
------------------------------------------------------------------


Get App hosting network utilization from device

.. code:: python

    def get_app_hosting_network_utils(device_id: str) -> Any: ...


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
        client.device.app_hosting.network_utilization.get_app_hosting_network_utils()


