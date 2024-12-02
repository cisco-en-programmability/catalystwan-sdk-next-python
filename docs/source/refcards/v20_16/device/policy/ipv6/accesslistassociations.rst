=========================================
device.policy.ipv6.accesslistassociations
=========================================


Operation: GET /dataservice/device/policy/ipv6/accesslistassociations
---------------------------------------------------------------------


Get access list associations from device

.. code:: python

    def create_policy_access_list_associations_ipv6(
        device_id: str,
    ) -> Any: ...


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
        client.device.policy.ipv6.accesslistassociations.create_policy_access_list_associations_ipv6()


