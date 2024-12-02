=========================================================
sdavc.protocol_pack.compliance.initiate_policy_compliance
=========================================================


Operation: POST /dataservice/sdavc/protocol-pack/compliance/initiate-policy-compliance
--------------------------------------------------------------------------------------


Initiate policy compliance task

.. code:: python

    def initiate_policy_compliance() -> None: ...


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
        client.sdavc.protocol_pack.compliance.initiate_policy_compliance.initiate_policy_compliance()


