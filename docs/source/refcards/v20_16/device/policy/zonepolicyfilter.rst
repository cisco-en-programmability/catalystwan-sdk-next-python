==============================
device.policy.zonepolicyfilter
==============================


Operation: GET /dataservice/device/policy/zonepolicyfilter
----------------------------------------------------------


Get zone policy filter from device

.. code:: python

    def get_zone_policy_filters(device_id: str) -> Any: ...


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
        client.device.policy.zonepolicyfilter.get_zone_policy_filters()


