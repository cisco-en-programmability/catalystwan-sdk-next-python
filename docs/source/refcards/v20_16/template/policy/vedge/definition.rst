================================
template.policy.vedge.definition
================================


Operation: GET /dataservice/template/policy/vedge/definition/{policyId}
-----------------------------------------------------------------------


Get template

.. code:: python

    def get(policy_id: str) -> Any: ...


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
        client.template.policy.vedge.definition.get()


