==============
device.cts_pac
==============


Operation: GET /dataservice/device/ctsPac
-----------------------------------------


get Cisco TrustSec PAC information from device

.. code:: python

    def get(device_id: str) -> Any: ...


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
        client.device.cts_pac.get()


