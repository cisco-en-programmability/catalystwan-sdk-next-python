=================================
device.policy.rewriteassociations
=================================


Operation: GET /dataservice/device/policy/rewriteassociations
-------------------------------------------------------------


Get rewrite associations information from device

.. code:: python

    def create_policy_rewrite_associations_info(
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
        client.device.policy.rewriteassociations.create_policy_rewrite_associations_info()


