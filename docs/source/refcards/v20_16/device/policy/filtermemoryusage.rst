===============================
device.policy.filtermemoryusage
===============================


Operation: GET /dataservice/device/policy/filtermemoryusage
-----------------------------------------------------------


Get data policy filter memory usage from device

.. code:: python

    def create_policy_filter_memory_usage(device_id: str) -> Any: ...


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
        client.device.policy.filtermemoryusage.create_policy_filter_memory_usage()


