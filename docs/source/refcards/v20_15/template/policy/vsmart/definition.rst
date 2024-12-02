=================================
template.policy.vsmart.definition
=================================


Operation: GET /dataservice/template/policy/vsmart/definition/{policyId}
------------------------------------------------------------------------


Get template policy definition by policy id

.. code:: python

    def get_template_by_policy_id(policy_id: str) -> Any: ...


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
        client.template.policy.vsmart.definition.get_template_by_policy_id()


