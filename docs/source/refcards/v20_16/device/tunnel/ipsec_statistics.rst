==============================
device.tunnel.ipsec_statistics
==============================


Operation: GET /dataservice/device/tunnel/ipsec_statistics
----------------------------------------------------------


Get tunnel IPSec statistics all devices

.. code:: python

    def create_ipsec_statistics_list(device_id: str) -> Any: ...


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
        client.device.tunnel.ipsec_statistics.create_ipsec_statistics_list()


