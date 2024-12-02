==========================
device.role_based_counters
==========================


Operation: GET /dataservice/device/roleBasedCounters
----------------------------------------------------


get Cisco TrustSec Role Based Counters information from device

.. code:: python

    def get_role_based_counters(device_id: str) -> Any: ...


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
        client.device.role_based_counters.get_role_based_counters()


