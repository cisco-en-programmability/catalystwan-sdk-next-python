================================
device.policy.accesslistpolicers
================================


Operation: GET /dataservice/device/policy/accesslistpolicers
------------------------------------------------------------


Get access list policers from device

.. code:: python

    def create_policy_access_list_policers(device_id: str) -> Any: ...


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
        client.device.policy.accesslistpolicers.create_policy_access_list_policers()


