===================================
template.policy.security.definition
===================================


Operation: GET /dataservice/template/policy/security/definition/{policyId}
--------------------------------------------------------------------------


Get Template

.. code:: python

    def get_security_template(policy_id: str) -> Any: ...


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
        client.template.policy.security.definition.get_security_template()


