=====================================
template.policy.definition.aclv6.bulk
=====================================


Operation: PUT /dataservice/template/policy/definition/aclv6/bulk
-----------------------------------------------------------------


Create/Edit policy definitions in bulk

.. code:: python

    def save_policy_definition_in_bulk_9(
        payload: Optional[Any] = None,
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
        client.template.policy.definition.aclv6.bulk.save_policy_definition_in_bulk_9()


