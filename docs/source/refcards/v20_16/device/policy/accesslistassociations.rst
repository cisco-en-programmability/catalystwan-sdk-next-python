====================================
device.policy.accesslistassociations
====================================


Operation: GET /dataservice/device/policy/accesslistassociations
----------------------------------------------------------------


Get access list associations from device

.. code:: python

    def create_policy_access_list_associations(device_id: str) -> Any: ...


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
        client.device.policy.accesslistassociations.create_policy_access_list_associations()


