============================================
sdavc.protocol_pack.compliance.policy.status
============================================


Operation: GET /dataservice/sdavc/protocol-pack/compliance/policy/status/{uuid}
-------------------------------------------------------------------------------


Get policy compliance status

.. code:: python

    def get_policy_compliance_status(uuid: str) -> Any: ...


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
        client.sdavc.protocol_pack.compliance.policy.status.get_policy_compliance_status()


