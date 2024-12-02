=================================================
template.policy.definition.ssldecryption.multiple
=================================================


Operation: PUT /dataservice/template/policy/definition/ssldecryption/multiple/{id}
----------------------------------------------------------------------------------


Edit multiple policy definitions

.. code:: python

    def edit_multiple_policy_definition_3(
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
        client.template.policy.definition.ssldecryption.multiple.edit_multiple_policy_definition_3()


