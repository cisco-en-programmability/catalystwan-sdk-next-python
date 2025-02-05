================================
template.policy.security.summary
================================


Operation: GET /dataservice/template/policy/security/summary
------------------------------------------------------------


Generate security policy summary

.. code:: python

    def generate_security_policy_summary() -> Any: ...


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
        client.template.policy.security.summary.generate_security_policy_summary()


