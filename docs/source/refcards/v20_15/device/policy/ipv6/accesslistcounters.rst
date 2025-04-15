=====================================
device.policy.ipv6.accesslistcounters
=====================================


Operation: GET /dataservice/device/policy/ipv6/accesslistcounters
-----------------------------------------------------------------


Get access list counters from device

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
        client.device.policy.ipv6.accesslistcounters.get()


