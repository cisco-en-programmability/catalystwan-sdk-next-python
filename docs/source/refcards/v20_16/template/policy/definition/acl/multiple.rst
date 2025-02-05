=======================================
template.policy.definition.acl.multiple
=======================================


Operation: PUT /dataservice/template/policy/definition/acl/multiple/{id}
------------------------------------------------------------------------


Edit multiple policy definitions

.. code:: python

    def edit_multiple_policy_definition_8(
        id: str, payload: Optional[Any] = None
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
        client.template.policy.definition.acl.multiple.edit_multiple_policy_definition_8()


