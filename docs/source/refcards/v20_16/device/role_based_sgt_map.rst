=========================
device.role_based_sgt_map
=========================


Operation: GET /dataservice/device/roleBasedSgtMap
--------------------------------------------------


get Cisco TrustSec Role Based SGT Map information from device

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
        client.device.role_based_sgt_map.get()


